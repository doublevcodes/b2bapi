from .rate_limit import RateLimitError
from .unauthorised import UnauthorisedError
from .invalid_token import InvalidTokenError
from .unknown import UnknownError
from typing import Union
import requests
import aiohttp

def response_check(response: Union[requests.Response, aiohttp.ClientResponse], token: str):
    if isinstance(response, requests.Response):
        if response.status_code == 429:
            raise RateLimitError(token=token)
        if response.status_code == 401:
            raise UnauthorisedError
        raise UnknownError
    if isinstance(response, aiohttp.ClientResponse):
        if response.status == 429:
            raise RateLimitError(token=token)
        if response.status == 401:
            raise UnauthorisedError
        raise UnknownError

def token_check(token: str):
    if len(token) != 25:
        raise InvalidTokenError(token)
    if token[4] != '.':
        raise InvalidTokenError(token)
    check_ret = requests.get('https://api.bytestobits.dev/info', headers={'Authorization': token})
    if check_ret.status_code == 401:
        raise InvalidTokenError(token)
    