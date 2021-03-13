from .rate_limit import RateLimitError
from .unauthorised import UnauthorisedError
import requests

def response_check(response: requests.Response):
    if response.status_code == 429:
        raise RateLimitError
    elif response.status_code == 401:
        raise UnauthorisedError