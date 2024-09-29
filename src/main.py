from configs.app_config import create_app_config
from di.container import Container
from src.rest_api.api import create_app


def create_container():
    container = Container()
    container.config.from_dict(create_app_config().model_dump())
    print(create_app_config().model_dump()["product_repository"]["service"].value)
    container.wire(modules=[__name__, "src.rest_api.api"])
    return container


container = create_container()

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
