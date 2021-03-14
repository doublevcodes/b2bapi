
class UnknownError(Exception):

    def __init__(self):
        super().__init__("We encountered an unknown error. Please try again.")
