import re
import os
from dataclasses import dataclass


@dataclass
class OpenAIImageRecognitionServiceConfig:
    api_key: str = os.environ.get("OPENAI_API_KEY")
    model: str = "gpt-4o"
    prompt: str = (
        """You will be given an image of the packaging of a product. Your task is to extract the nutritional information from the image and return it in a JSON format. The JSON should have the following structure: { 'kcal_100g': <kcal_100g>, 'proteins_100g': <proteins_100g>, 'carbs_100g': <carbs_100g>, 'fats_100g': <fats_100g> }.
        If there is no such information, return an empty JSON object.
        Output the answer inside <nutriments_json> tags and skip any preamble."""
    )
    nutriments_pattern = re.compile(
        r"<nutriments_json>(.*?)</nutriments_json>", re.DOTALL
    )
