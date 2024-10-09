from src.core.exceptions import BaseError


class AnalyticsError(BaseError):
    pass


class SumOfDailyIntakesAnalyticsServiceError(AnalyticsError):
    pass
