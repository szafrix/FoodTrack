from pydantic import BaseModel
from abc import ABC, abstractmethod


class ImageRecognitionInput(BaseModel):
    photo: str


class ImageRecognitionOutput(BaseModel):
    kcal_100g: float
    proteins_100g: float
    carbs_100g: float
    fats_100g: float


class ImageRecognitionService(ABC):
    @abstractmethod
    def read_nutriments_from_photo(
        self, input_: ImageRecognitionInput
    ) -> ImageRecognitionOutput:
        pass
