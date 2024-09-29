from src.core.services.image_recognition import (
    ImageRecognitionService,
    ImageRecognitionInput,
    ImageRecognitionOutput,
)


class DummyImageRecognitionService(ImageRecognitionService):
    def read_nutrients_from_image(
        self, input_: ImageRecognitionInput
    ) -> ImageRecognitionOutput:
        return ImageRecognitionOutput(
            success=True,
            kcal_100g=200,
            proteins_100g=200,
            carbs_100g=200,
            fats_100g=200,
            error=None,
        )
