from src.core.services.image_recognition.service import (
    ImageRecognitionService,
    ImageRecognitionInput,
    ImageRecognitionOutput,
)
from numpy import random


class DummyImageRecognitionService(ImageRecognitionService):
    def read_nutriments_from_photo(
        self, input_: ImageRecognitionInput
    ) -> ImageRecognitionOutput:
        return ImageRecognitionOutput(
            kcal_100g=random.randint(100, 200),
            proteins_100g=random.randint(10, 20),
            carbs_100g=random.randint(20, 30),
            fats_100g=random.randint(30, 40),
        )
