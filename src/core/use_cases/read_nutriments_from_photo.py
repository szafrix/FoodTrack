from logging import getLogger
from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.services.image_recognition.service import (
    ImageRecognitionService,
    ImageRecognitionInput,
)
from src.core.exceptions import BaseError, UnexpectedError


logger = getLogger(__name__)


class ReadNutrimentsFromPhotoUseCaseInput(BaseModel):
    name: str
    photo: str


class ReadNutrimentsFromPhotoUseCaseOutput(BaseModel):
    product: Product


class ReadNutrimentsFromPhotoUseCase:
    def __init__(self, image_recognition_service: ImageRecognitionService):
        self.image_recognition_service = image_recognition_service

    def execute(
        self, input_: ReadNutrimentsFromPhotoUseCaseInput
    ) -> ReadNutrimentsFromPhotoUseCaseOutput:
        try:
            image_recognition_input = ImageRecognitionInput(photo=input_.photo)
            image_recognition_response = (
                self.image_recognition_service.read_nutriments_from_photo(
                    image_recognition_input
                )
            )
            product = Product(
                name=input_.name,
                kcal_100g=image_recognition_response.kcal_100g,
                proteins_100g=image_recognition_response.proteins_100g,
                carbs_100g=image_recognition_response.carbs_100g,
                fats_100g=image_recognition_response.fats_100g,
            )
            return ReadNutrimentsFromPhotoUseCaseOutput(product=product)
        except BaseError as exc:
            logger.error(exc, exc_info=True)
            raise exc
        except Exception as exc:
            logger.error(
                f"Unexpected error while reading nutriments from photo {exc}",
                exc_info=True,
            )
            raise UnexpectedError(
                f"Unexpected error while reading nutriments from photo"
            ) from exc
