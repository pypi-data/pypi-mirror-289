import os
import re
import ast
import importlib
from datetime import datetime
from abc import ABC, abstractmethod

from datastorage import extract_all_imports, extract_relevant_imports, format_imports

class CodeGenerator(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_code(self, prompt: str) -> str:
        relevant_imports = self.extract_relevant_imports(prompt)
        all_imports = self.extract_all_imports()
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
    
    @abstractmethod
    def get_model_response(self, full_prompt: str):
        pass

    def extract_relevant_imports(self, prompt: str):
        return extract_relevant_imports(prompt)
    
    def extract_all_imports(self):
        return extract_all_imports()
    
    def format_imports(self, imports):
        return format_imports(imports)

    def validate_imports(self, code: str):
        lines = code.split('\n')
        for line in lines:
            if line.startswith("import ") or line.startswith("from "):
                try:
                    importlib.import_module(line.split()[1])
                except ImportError as e:
                    raise ValueError(f"Import error in generated code: {e}")
    
    def log_code(self, prompt: str, code: str):
        directory = 'generated_code'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        log_filename = os.path.join(directory, f'{self.model_name}_code_log.txt')
        
        with open(log_filename, 'a') as file:
            file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("User Prompt:\n")
            file.write(prompt + "\n\n")
            file.write("Generated Code:\n")
            file.write(code + "\n\n")
            file.write("="*80 + "\n\n")
    
    def parse_response(self, response):

        if 'text' in response:
            return response['text']
        elif 'choices' in response:
            return response['choices'][0]['message']['content'].strip()
        else:
            raise ValueError("Unexpected response format.")
