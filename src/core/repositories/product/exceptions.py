from src.core.exceptions import BaseError


class ProductRepositoryError(BaseError):
    pass


class SearchProductsForAutocompletionError(ProductRepositoryError):
    pass


class SaveProductError(ProductRepositoryError):
    pass
