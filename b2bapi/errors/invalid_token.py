
class InvalidTokenError(Exception):

    def __init__(self, token: str, message: str = "This token is invalid"):
        self.token = token
        self.message = message
        super().__init__()

    def __str__(self):
        return f'{self.message}: {self.token}'
