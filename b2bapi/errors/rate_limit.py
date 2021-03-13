
class RateLimitError(Exception):

    def __init__(self, status_code: int = 429, message: str = "You have been rate limited, please try again later"):
        self.status_code = status_code
        self.message = message
        super().__init__()

    def __str__(self):
        return f'{self.status_code}: {self.message}'
