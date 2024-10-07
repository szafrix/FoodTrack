from fastapi import Request, status
from fastapi.responses import JSONResponse
from src.core.exceptions import BaseError, UnexpectedError
from src.core.repositories.intake.exceptions import IntakeRepositoryError
from src.core.repositories.product.exceptions import ProductRepositoryError
from src.core.services.image_recognition.exceptions import ImageRecognitionServiceError
import traceback


async def error_handler_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except BaseError as e:
        if isinstance(e, IntakeRepositoryError):
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        elif isinstance(e, ProductRepositoryError):
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        elif isinstance(e, ImageRecognitionServiceError):
            status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        else:
            status_code = status.HTTP_400_BAD_REQUEST

        return JSONResponse(
            status_code=status_code,
            content={
                "error": str(e),
                "error_type": e.__class__.__name__,
                "stack_trace": traceback.format_exc(),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": "An unexpected error occurred",
                "error_type": "UnexpectedError",
                "stack_trace": traceback.format_exc(),
            },
        )
