from abc import ABC, abstractmethod
from pydantic import BaseModel


class ImageRecognitionInput(BaseModel):
    image: str


class ImageRecognitionOutput(BaseModel):
    success: bool
    kcal_100g: float | None
    proteins_100g: float | None
    carbs_100g: float | None
    fats_100g: float | None
    error: str | None


class ImageRecognitionService(ABC):
    @abstractmethod
    def read_nutrients_from_image(
        self, input_: ImageRecognitionInput
    ) -> ImageRecognitionOutput:
        pass
