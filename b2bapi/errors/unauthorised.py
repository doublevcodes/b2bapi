
class UnauthorisedError(Exception):

    def __init__(self, code: int = 401, message: str = "Invalid token or no token provided"):
        self.code = code
        self.message = message
        super().__init__()

    def __str__(self):
        return f'{self.code}: {self.message}'
        