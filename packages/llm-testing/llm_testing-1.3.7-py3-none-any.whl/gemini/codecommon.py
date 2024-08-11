import os
import re
import ast
import importlib
from datetime import datetime
from abc import ABC, abstractmethod
import pandas as pd

diagrams_data = {}


def extract_relevant_imports(prompt: str) -> dict:
    relevant_imports = {}
    for category, components in diagrams_data.items():
        for component in components:
            if component.lower() in prompt.lower():
                relevant_imports.setdefault(category, []).append(component)
    return relevant_imports

def extract_all_imports() -> dict:
    irrelevant_imports = {category: components for category, components in diagrams_data.items()}
    return irrelevant_imports

def format_imports(relevant_imports: dict) -> str:
    imports_code = []
    for category, components in relevant_imports.items():
        base_module = ".".join(category.split(".")[:-1])
        class_name = category.split(".")[-1]
        components_str = ", ".join(components)
        imports_code.append(f"from {base_module} import {class_name}\n{class_name} = [{components_str}]")
    return "\n".join(imports_code)

class CodeGenerator(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_code(self, prompt: str) -> str:
        relevant_imports = self.extract_relevant_imports(prompt)
        formatted_imports = self.format_imports(relevant_imports)
        
        full_prompt = (
            f"Generate a complete Python script using the diagrams package to create a system diagram. "
            f"The script should only use the following imports:\n\n{formatted_imports}.\n\n"
            f"Do not use any imports outside of {formatted_imports}. If additional functionality is needed, provide a comment instead. "
            f"Ensure the output image is always saved as 'diagram_output'. Only return the complete Python code wrapped in triple backticks.\n\n"
            f"User prompt: {prompt}"
        )

        response = self.get_model_response(full_prompt)
        content = self.parse_response(response)
        
        code_match = re.search(r'```(?:python)?(.*?)```', content, re.DOTALL)
        if code_match:
            code = code_match.group(1).strip()

            try:
                ast.parse(code)
            except SyntaxError as e:
                raise ValueError(f"Syntax error in generated code: {e}")
            
            self.validate_imports(code)
            self.log_code(prompt, code)

            return code
        else:
            raise ValueError("No code block found in the response.")
        

    def generate_text(self, prompt: str) -> str:
        full_prompt = (
            f"Please generate a detailed and relevant text-based response based on the following prompt:\n\n"
            f"{prompt}\n\n"
        )

        response = self.get_model_response(full_prompt)
        content = self.parse_response(response)
        

        self.log_text(prompt, content)
        return content     


    def generate_code_general(self, prompt: str) -> str:
        full_prompt = (
            f"Generate a complete and valid code snippet based on the following prompt:\n\n"
            f"{prompt}\n\n"
            f"Ensure the code is syntactically correct and complete, wrapped in triple backticks."
        )

        response = self.get_model_response(full_prompt)
        content = self.parse_response(response)
        
        code_match = re.search(r'```(?:\w+)?(.*?)```', content, re.DOTALL)
        if code_match:
            code = code_match.group(1).strip()
            return code
        else:
            raise ValueError("No code block found in the response.")       
    
    @abstractmethod
    def get_model_response(self, full_prompt: str):
        pass

    def extract_relevant_imports(self, prompt: str):
        return extract_relevant_imports(prompt)
    
    def format_imports(self, imports):
        return format_imports(imports)

    def validate_imports(self, code: str):
        for line in code.split('\n'):
            if line.startswith("import ") or line.startswith("from "):
                try:
                    importlib.import_module(line.split()[1])
                except ImportError as e:
                    raise ValueError(f"Import error in generated code: {e}")

    def log_text(self, prompt: str, content: str, format: str = "txt"):
        directory = 'generated_text'
        os.makedirs(directory, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if format == "txt":
            log_filename = os.path.join(directory, f'{self.model_name}_text_log.txt')
            with open(log_filename, 'a') as file:
                file.write(f"Timestamp: {timestamp}\n")
                file.write("User Prompt:\n")
                file.write(prompt + "\n\n")
                file.write("Generated Text:\n")
                file.write(content + "\n\n")
                file.write("="*80 + "\n\n")
        elif format == "excel":
            log_filename = os.path.join(directory, f'{self.model_name}_text_log.xlsx')
            df = pd.DataFrame([[timestamp, prompt, content]], columns=["Timestamp", "User Prompt", "Generated Text"])
            if os.path.exists(log_filename):
                with pd.ExcelWriter(log_filename, mode="a", if_sheet_exists="overlay") as writer:
                    df.to_excel(writer, sheet_name="TextLog", index=False, header=False, startrow=writer.sheets["TextLog"].max_row)
            else:
                with pd.ExcelWriter(log_filename) as writer:
                    df.to_excel(writer, sheet_name="TextLog", index=False)

    def log_code(self, prompt: str, code: str, format: str = "txt"):
        directory = 'generated_code'
        os.makedirs(directory, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if format == "txt":
            log_filename = os.path.join(directory, f'{self.model_name}_code_log.txt')
            with open(log_filename, 'a') as file:
                file.write(f"Timestamp: {timestamp}\n")
                file.write("User Prompt:\n")
                file.write(prompt + "\n\n")
                file.write("Generated Code:\n")
                file.write(code + "\n\n")
                file.write("="*80 + "\n\n")
        elif format == "excel":
            log_filename = os.path.join(directory, f'{self.model_name}_code_log.xlsx')
            df = pd.DataFrame([[timestamp, prompt, code]], columns=["Timestamp", "User Prompt", "Generated Code"])
            if os.path.exists(log_filename):
                with pd.ExcelWriter(log_filename, mode="a", if_sheet_exists="overlay") as writer:
                    df.to_excel(writer, sheet_name="CodeLog", index=False, header=False, startrow=writer.sheets["CodeLog"].max_row)
            else:
                with pd.ExcelWriter(log_filename) as writer:
                    df.to_excel(writer, sheet_name="CodeLog", index=False)

    def parse_response(self, response):
        if 'text' in response:
            return response['text']
        elif 'choices' in response:
            return response['choices'][0]['message']['content'].strip()
        else:
            raise ValueError("Unexpected response format.")
