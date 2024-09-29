from dependency_injector import containers, providers
from src.configs.app_config import (
    AvailableImageRecognitionServices,
    AvailableProductRepositories,
)
from src.core.services.image_recognition import ImageRecognitionService
from src.core.repositories.product_repository import ProductRepository
from impl.services.dummy_image_recognition import DummyImageRecognitionService
from src.impl.repositories.dummy_product_repository import DummyProductRepository
from src.core.interactors.register_product import RegisterProductInteractor
from src.core.use_cases.register_product_in_repository import (
    RegisterProductInRepositoryUseCase,
)
from src.core.use_cases.fetch_product_from_repository import (
    GetProductFromRepositoryUseCase,
)


def create_image_recognition_service(
    service: AvailableImageRecognitionServices,
) -> ImageRecognitionService:
    if service.value == AvailableImageRecognitionServices.DUMMY.value:
        return DummyImageRecognitionService()
    else:
        raise ValueError(f"Invalid image recognition service: {service.value}")


def create_product_repository_service(
    service: AvailableProductRepositories,
) -> ProductRepository:
    if service.value == AvailableProductRepositories.DUMMY.value:
        return DummyProductRepository()
    else:
        raise ValueError(f"Invalid product repository service: {service.value}")


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    image_recognition_service = providers.Factory(
        create_image_recognition_service,
        service=config.image_recognition.service,
    )

    product_repository_service = providers.Factory(
        create_product_repository_service,
        service=config.product_repository.service,
    )

    register_product_use_case = providers.Factory(
        RegisterProductInRepositoryUseCase,
        product_repository=product_repository_service,
    )

    get_product_use_case = providers.Factory(
        GetProductFromRepositoryUseCase,
        product_repository=product_repository_service,
    )

    register_product_Interactor = providers.Factory(
        RegisterProductInteractor,
        register_product_use_case=register_product_use_case,
        get_product_use_case=get_product_use_case,
        image_recognition_service=image_recognition_service,
    )
