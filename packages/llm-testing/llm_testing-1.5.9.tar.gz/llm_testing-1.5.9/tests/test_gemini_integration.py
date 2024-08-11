import pytest
from unittest.mock import patch, MagicMock
from gemini.gemini_integration import GeminiCodeGenerator

@pytest.fixture
def gemini_code_generator():
    return GeminiCodeGenerator()

def test_configure_api_key(gemini_code_generator):
    with patch('gemini_integration.get_google_api_key') as mock_get_google_api_key:
        mock_get_google_api_key.return_value = "mocked_api_key"
        gemini_code_generator.configure_api_key()
        mock_get_google_api_key.assert_called_once()

@patch('gemini_integration.genai.GenerativeModel')
def test_get_model_response(mock_generative_model_class, gemini_code_generator):
    mock_generative_model = MagicMock()
    mock_generative_model.generate_content.return_value.text = "Generated Code"
    mock_generative_model_class.return_value = mock_generative_model
    
    prompt = "Generate a simple diagram"
    response = gemini_code_generator.get_model_response(prompt)
    
    mock_generative_model_class.assert_called_once_with('gemini-1.5-pro')
    mock_generative_model.generate_content.assert_called_once_with(prompt)
    assert response['text'] == "Generated Code"

def test_generate_code(gemini_code_generator):
    mock_response = {
        'choices': [{
            'message': {
                'content': "```python\n# Some generated code\n```"
            }
        }]
    }
    with patch.object(gemini_code_generator, 'get_model_response', return_value=mock_response):
        prompt = "Create a system diagram with AWS EC2 and ELB."
        generated_code = gemini_code_generator.generate_code(prompt)
        assert "# Some generated code" in generated_code
        assert "EC2" in generated_code
        assert "ELB" in generated_code

@patch('builtins.open', new_callable=MagicMock)
def test_log_code(mock_open, gemini_code_generator):
    prompt = "Generate a simple diagram"
    code = "# Some generated code"
    
    gemini_code_generator.log_code(prompt, code)
    
    mock_open.assert_called_once_with('generated_code/gemini_code_log.txt', 'a')
    mock_open().write.assert_any_call(f"User Prompt:\n{prompt}\n\n")
    mock_open().write.assert_any_call(f"Generated Code:\n{code}\n\n")

if __name__ == "__main__":
    pytest.main()
