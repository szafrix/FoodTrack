from dependency_injector import containers, providers
from src.configs.app_config import (
    ImageRecognitionConfig,
    IntakeRepositoryConfig,
    ProductRepositoryConfig,
    ImageRecognitionServices,
    IntakeRepositories,
    ProductRepositories,
    AnalyticsConfig,
    AnalyticsServices,
)
from src.core.repositories.product.repository import ProductRepository
from src.core.repositories.intake.repository import IntakeRepository
from src.core.services.image_recognition.service import ImageRecognitionService
from src.core.use_cases.register_intake import RegisterIntakeUseCase
from src.core.use_cases.register_product_in_repository import (
    RegisterProductInRepositoryUseCase,
)
from src.core.use_cases.fetch_products_for_autocompletion import (
    FetchProductsForAutocompletionUseCase,
)
from src.core.use_cases.read_nutriments_from_photo import (
    ReadNutrimentsFromPhotoUseCase,
)
from src.core.use_cases.get_daily_sum_of_intakes import (
    GetDailySumOfIntakesUseCase,
)
from src.core.services.analytics.service import AnalyticsService


def get_product_repository(config: ProductRepositoryConfig) -> ProductRepository:
    match config.name:
        case ProductRepositories.DUMMY:
            from src.impl.repositories.product.dummy.repository import (
                DummyProductRepository,
            )

            return DummyProductRepository()
        case ProductRepositories.SQLITE:
            from src.impl.repositories.product.sqlite.repository import (
                SQLiteProductRepository,
            )
            from src.impl.repositories.product.sqlite.config import (
                SQLiteProductRepositoryConfig,
            )

            return SQLiteProductRepository(SQLiteProductRepositoryConfig())
        case _:
            raise ValueError(f"Invalid product repository name: {config.name}")


def get_intake_repository(config: IntakeRepositoryConfig) -> IntakeRepository:
    match config.name:
        case IntakeRepositories.DUMMY:
            from src.impl.repositories.intake.dummy.repository import (
                DummyIntakeRepository,
            )

            return DummyIntakeRepository()
        case IntakeRepositories.SQLITE:
            from src.impl.repositories.intake.sqlite.repository import (
                SQLiteIntakeRepository,
            )
            from src.impl.repositories.intake.sqlite.config import (
                SQLiteIntakeRepositoryConfig,
            )

            return SQLiteIntakeRepository(SQLiteIntakeRepositoryConfig())
        case _:
            raise ValueError(f"Invalid intake repository name: {config.name}")


def get_image_recognition_service(
    config: ImageRecognitionConfig,
) -> ImageRecognitionService:
    match config.name:
        case ImageRecognitionServices.DUMMY:
            from src.impl.services.image_recognition.dummy.service import (
                DummyImageRecognitionService,
            )

            return DummyImageRecognitionService()
        case ImageRecognitionServices.OPENAI:
            from src.impl.services.image_recognition.openai.service import (
                OpenAIImageRecognitionService,
            )
            from src.impl.services.image_recognition.openai.config import (
                OpenAIImageRecognitionServiceConfig,
            )

            return OpenAIImageRecognitionService(OpenAIImageRecognitionServiceConfig())
        case _:
            raise ValueError(f"Invalid image recognition service name: {config.name}")


def get_analytics_service(config: AnalyticsConfig, intake_repository: IntakeRepository, product_repository: ProductRepository) -> AnalyticsService:
    match config.name:
        case AnalyticsServices.DUMMY:
            from src.impl.services.analytics.dummy.service import (
                DummyAnalyticsService,
            )

            return DummyAnalyticsService(intake_repository, product_repository)
        case AnalyticsServices.SQLITE:
            from src.impl.services.analytics.sqlite.service import (
                SqliteAnalyticsService,
            )

            return SqliteAnalyticsService(intake_repository, product_repository)
        case _:
            raise ValueError(f"Invalid analytics service name: {config.name}")
        


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    product_repository = providers.Singleton(
        get_product_repository,
        config=config.product_repository.as_(ProductRepositoryConfig),
    )
    intake_repository = providers.Singleton(
        get_intake_repository,
        config=config.intake_repository.as_(IntakeRepositoryConfig),
    )
    image_recognition_service = providers.Singleton(
        get_image_recognition_service,
        config=config.image_recognition.as_(ImageRecognitionConfig),
    )
    analytics_service = providers.Singleton(
        get_analytics_service,
        config=config.analytics.as_(AnalyticsConfig),
        intake_repository=intake_repository,
        product_repository=product_repository,
    )

    register_intake_use_case = providers.Factory(
        RegisterIntakeUseCase,
        intake_repository=intake_repository,
    )

    register_product_in_repository_use_case = providers.Factory(
        RegisterProductInRepositoryUseCase,
        product_repository=product_repository,
    )

    fetch_products_for_autocompletion_use_case = providers.Factory(
        FetchProductsForAutocompletionUseCase,
        product_repository=product_repository,
    )

    read_nutriments_from_photo_use_case = providers.Factory(
        ReadNutrimentsFromPhotoUseCase,
        image_recognition_service=image_recognition_service,
    )

    get_daily_sum_of_intakes_use_case = providers.Factory(
        GetDailySumOfIntakesUseCase,
        analytics_service=analytics_service,
    )
