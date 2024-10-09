from src.configs.app_config import AppConfig
from src.di.container import Container
from src.rest_api.api import create_app
import uvicorn
import logging
from src.deployment.ngrok.service import NgrokService

logger = logging.getLogger(__name__)


def create_container(app_config: AppConfig):
    container = Container()
    container.config.from_dict(app_config.model_dump())
    container.wire(
        modules=[
            __name__,
            "src.rest_api.api",
            "src.rest_api.endpoints.product.register_product_image",
            "src.rest_api.endpoints.product.register_product_manual",
            "src.rest_api.endpoints.intake.register",
            "src.rest_api.endpoints.autocomplete",
            "src.rest_api.endpoints.analytics.daily_sum_of_intakes",
        ]
    )
    return container


def create_allowed_origins(app_config: AppConfig, ngrok_service: NgrokService):
    allowed_origins = [f"http://{app_config.rest_api.host}:{app_config.rest_api.port}"]
    if app_config.ngrok.use_ngrok:
        allowed_origins.append(ngrok_service.listener.url())
    return allowed_origins


app_config = AppConfig()
container = create_container(app_config)

ngrok_service = NgrokService(app_config)
ngrok_service.start_ngrok()
allowed_origins = create_allowed_origins(app_config, ngrok_service)
app = create_app(allowed_origins)

if __name__ == "__main__":
    uvicorn.run(app, host=app_config.rest_api.host, port=app_config.rest_api.port)
