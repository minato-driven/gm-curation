import os
import google.generativeai as genai
from gateway import Gateway


class GeminiGateway(Gateway):
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key not found. Please set GEMINI_API_KEY in your environment."
            )

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def get_text_content(self, prompt: str) -> str:
        """
        Generates text content based on the provided prompt.
        """
        response = self.model.generate_content(prompt)
        self.log(f"prompt: {prompt}")
        self.log(f"response: {response.text}")
        return response.text

    def get_json_content(self, prompt: str) -> str:
        """
        Generates JSON content based on the provided prompt.
        Returns the raw JSON string.
        """
        generation_config = genai.types.GenerationConfig(
            response_mime_type="application/json"
        )
        response = self.model.generate_content(
            prompt, generation_config=generation_config
        )
        self.log(f"prompt: {prompt}")
        self.log(f"response: {response.text}")
        return response.text
