import os
from codecommon import CodeGenerator
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class GeminiCodeGenerator(CodeGenerator):
    def __init__(self):
        super().__init__('gemini')

    def get_model_response(self, full_prompt: str):
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(full_prompt)
        return {"text": response.text.strip()}


if __name__ == "__main__":
    generator = GeminiCodeGenerator()
    prompt = "Create a system diagram for a web application with user authentication and data storage."
    code = generator.generate_code(prompt)
    print(code)
