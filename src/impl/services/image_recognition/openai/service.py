import requests
import json
from typing import Dict
from src.core.services.image_recognition.service import (
    ImageRecognitionService,
    ImageRecognitionInput,
    ImageRecognitionOutput,
)
from src.impl.services.image_recognition.openai.config import (
    OpenAIImageRecognitionServiceConfig,
)
from openai import OpenAI
from src.core.services.image_recognition.exceptions import ImageRecognitionServiceError


class OpenAIImageRecognitionService(ImageRecognitionService):
    def __init__(self, config: OpenAIImageRecognitionServiceConfig):
        self.config = config
        self.client = OpenAI(api_key=config.api_key)

    def read_nutriments_from_photo(
        self, input_: ImageRecognitionInput
    ) -> ImageRecognitionOutput:
        try:
            response = self.get_response(input_.photo)
            nutriments = self.extract_nutriments_from_response(response)
            return self.build_response(nutriments)
        except Exception as exc:
            raise ImageRecognitionServiceError(
                f"Error reading nutriments from photo"
            ) from exc

    def get_response(self, photo: str) -> str:
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": self.config.prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{photo}"},
                        },
                    ],
                }
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content

    def extract_nutriments_from_response(self, response: str) -> Dict[str, float]:
        match = self.config.nutriments_pattern.search(response)
        if match:
            return json.loads(match.group(1))
        return {}

    def build_response(self, nutriments: Dict[str, float]) -> ImageRecognitionOutput:
        return ImageRecognitionOutput(**nutriments)
