from pydantic import BaseModel
from src.core.entities.product import Product
from src.core.services.image_recognition import (
    ImageRecognitionService,
    ImageRecognitionInput,
)
from src.core.use_cases.register_product_in_repository import (
    RegisterProductInRepositoryUseCase,
    RegisterProductInRepositoryUseCaseInput,
)
from src.core.use_cases.fetch_product_from_repository import (
    GetProductFromRepositoryUseCase,
    GetProductFromRepositoryUseCaseInput,
)


from pydantic import BaseModel, model_validator, computed_field


class RegisterProductInteractorInput(BaseModel):
    name: str
    kcal_100g: float | None = None
    proteins_100g: float | None = None
    carbs_100g: float | None = None
    fats_100g: float | None = None
    nutrients_image: str | None = None
    try_to_fetch_product: bool

    @computed_field
    @property
    def is_image_provided(self) -> bool:
        return self.nutrients_image is not None

    @computed_field
    @property
    def is_nutrients_provided(self) -> bool:
        return all(
            getattr(self, field) is not None
            for field in ["kcal_100g", "proteins_100g", "carbs_100g", "fats_100g"]
        )

    @model_validator(mode="after")
    def validate_nutrients_or_image(self):
        if not (self.is_image_provided or self.is_nutrients_provided):
            raise ValueError(
                "Either nutrients_image or at least one nutrient value must be provided"
            )
        return self


class RegisterProductInteractorOutput(BaseModel):
    success: bool
    error: str | None
    is_fetched_from_repository: bool


class RegisterProductInteractor:
    def __init__(
        self,
        register_product_use_case: RegisterProductInRepositoryUseCase,
        get_product_use_case: GetProductFromRepositoryUseCase,
        image_recognition_service: ImageRecognitionService,
    ):
        self.register_product_use_case = register_product_use_case
        self.get_product_use_case = get_product_use_case
        self.image_recognition_service = image_recognition_service

    def execute(
        self, input_: RegisterProductInteractorInput
    ) -> RegisterProductInteractorOutput:
        if input_.try_to_fetch_product:
            fetch_product_input = GetProductFromRepositoryUseCaseInput(
                product_name=input_.name
            )
            fetch_product_output = self.get_product_use_case.execute(
                fetch_product_input
            )
            if fetch_product_output.success:
                return RegisterProductInteractorOutput(
                    success=True,
                    is_fetched_from_repository=True,
                    error=None,
                )
        if input_.is_nutrients_provided:
            product = Product(
                name=input_.name,
                kcal_100g=input_.kcal_100g,
                proteins_100g=input_.proteins_100g,
                carbs_100g=input_.carbs_100g,
                fats_100g=input_.fats_100g,
            )
            use_case_input = RegisterProductInRepositoryUseCaseInput(product=product)
            return self.register_product_use_case.execute(use_case_input)
        else:
            image_recognition_input = ImageRecognitionInput(
                image=input_.nutrients_image
            )
            image_recognition_output = (
                self.image_recognition_service.read_nutrients_from_image(
                    image_recognition_input
                )
            )
            product = Product(
                name=input_.name,
                kcal_100g=image_recognition_output.kcal_100g,
                proteins_100g=image_recognition_output.proteins_100g,
                carbs_100g=image_recognition_output.carbs_100g,
                fats_100g=image_recognition_output.fats_100g,
            )
            use_case_input = RegisterProductInRepositoryUseCaseInput(product=product)
            if image_recognition_output.success:
                return self.register_product_use_case.execute(use_case_input)
            else:
                return RegisterProductInteractorOutput(
                    success=False,
                    is_fetched_from_repository=False,
                    error=image_recognition_output.error,
                )
