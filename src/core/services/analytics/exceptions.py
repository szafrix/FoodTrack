from src.core.exceptions import BaseError


class AnalyticsError(BaseError):
    pass


class DailySumOfIntakesAnalyticsServiceError(AnalyticsError):
    pass
