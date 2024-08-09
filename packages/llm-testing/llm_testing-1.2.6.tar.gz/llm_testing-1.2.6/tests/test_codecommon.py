import pytest
from unittest import mock
import os
import importlib
from gemini.codecommon import CodeGenerator, extract_relevant_imports, format_imports

# Define a mock diagrams_data to be used in the tests
mock_diagrams_data = {
    'diagrams.aws.compute': ['EC2'],
    'diagrams.aws.network': ['ELB'],
    'diagrams.programming.language': ['C', 'R']
}

# Mock the diagrams_data within the CodeGenerator module
@mock.patch('codecommon.diagrams_data', mock_diagrams_data)
class MockCodeGenerator(CodeGenerator):
    def get_model_response(self, full_prompt: str):
        return {
            'choices': [{
                'message': {
                    'content': "```python\n# Some code\n```"
                }
            }]
        }

@pytest.fixture
def code_generator():
    return MockCodeGenerator(model_name="mock_model")

def test_extract_relevant_imports(code_generator):
    prompt = "Create a diagram with AWS EC2 and ELB."
    expected_imports = {
        'diagrams.aws.compute': ['EC2'],
        'diagrams.aws.network': ['ELB']
    }
    extracted_imports = code_generator.extract_relevant_imports(prompt)
    assert extracted_imports == expected_imports

def test_format_imports(code_generator):
    imports = {
        'diagrams.aws.compute': ['EC2'],
        'diagrams.aws.network': ['ELB']
    }
    formatted_imports = code_generator.format_imports(imports)
    expected_code = "from diagrams.aws import compute\ncompute = [EC2]\nfrom diagrams.aws import network\nnetwork = [ELB]"
    assert formatted_imports == expected_code

def test_validate_imports(code_generator):
    valid_code = """
    from diagrams.aws.compute import EC2
    from diagrams.aws.network import ELB
    """
    code_generator.validate_imports(valid_code)  # Should pass without exception

    invalid_code = """
    from nonexistentmodule import NonExistentClass
    """
    with pytest.raises(ValueError, match="Import error in generated code"):
        code_generator.validate_imports(invalid_code)

def test_log_code(code_generator):
    prompt = "Create a diagram with AWS EC2 and ELB."
    code = "from diagrams.aws.compute import EC2\nfrom diagrams.aws.network import ELB"
    
    log_dir = 'generated_code'
    log_filename = os.path.join(log_dir, f'{code_generator.model_name}_code_log.txt')
    
    # Ensure the directory is empty before testing
    if os.path.exists(log_filename):
        os.remove(log_filename)
    
    code_generator.log_code(prompt, code)
    
    assert os.path.exists(log_filename)
    
    with open(log_filename, 'r') as file:
        content = file.read()
        assert prompt in content
        assert code in content

def test_parse_response(code_generator):
    mock_response = {
        'choices': [{
            'message': {
                'content': "```python\n# Some code\n```"
            }
        }]
    }
    parsed_content = code_generator.parse_response(mock_response)
    assert parsed_content == "# Some code"
