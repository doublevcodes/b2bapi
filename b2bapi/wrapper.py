import requests
import aiohttp
from typing import Optional
from .meme import Meme
from .madlib import Madlib
from .text import Text
from .word import Word
from .errors.response_check import response_check, token_check


class BytesToBits:

    def __init__(self, token: str) -> None:
        self.auth_header = {
            'Authorization': token
        }
        token_check(token)
        self.token = token
        self.BASE_URL = 'https://api.bytestobits.dev'
        return

    def get_word(self) -> Word:
        "Returns a random word from the API"
        ret = requests.get(f'{self.BASE_URL}/word/', headers=self.auth_header)
        response_check(ret, self.token)
        return Word(ret.json())

    def get_text(self) -> Text:
        "Returns a random paragraph from the API"
        ret = requests.get(f'{self.BASE_URL}/text/', headers=self.auth_header)
        response_check(ret, self.token)
        return Text(ret.json())

    def get_meme(self) -> Meme:
        "Returns a random meme from a random subreddit through the API"
        ret = requests.get(f'{self.BASE_URL}/meme/', headers=self.auth_header)
        response_check(ret, self.token)
        ret = ret.json()
        return Meme(ret['title'], ret['url'], ret['link'], ret['subreddit'])

    def get_madlib(self) -> Madlib:
        "Returns a random madlib from the API"
        ret = requests.get(f'{self.BASE_URL}/madlibs/', headers=self.auth_header)
        response_check(ret, self.token)
        ret = ret.json()
        return Madlib(ret['title'], ret['text'], ret['questions'], ret['variables'])


class AsynchronousBytesToBits:
    def __init__(self, token: str, session: Optional[aiohttp.ClientSession] = None) -> None:
        self.auth_header = {
            'Authorization': token
        }
        token_check(token)
        self.token = token
        self.BASE_URL = 'https://api.bytestobits.dev'
        if not session:
            self.session = aiohttp.ClientSession()
        else:
            self.session = session
        return

    async def get_word(self) -> Word:
        "Returns a random word from the API in an asynchronous context"
        async with self.session.get(f'{self.BASE_URL}/word/', headers=self.auth_header) as request:
            return Word(await request.json())

    async def get_text(self) -> Text:
        "Returns a random paragraph from the API in an asynchronous context"
        async with self.session.get(f'{self.BASE_URL}/text/', headers=self.auth_header) as request:
            return Text(await request.json())

    async def get_meme(self) -> Meme:
        "Returns a random meme from the API in an asynchronous context"
        async with self.session.get(f'{self.BASE_URL}/meme/', headers=self.auth_header) as request:
            ret = await request.json()
            return Meme(ret['title'], ret['url'], ret['link'], ret['subreddit'])

    async def get_madlib(self) -> Madlib:
        "Returns a random madlib from the API in an asynchronous context"
        async with self.session.get(f'{self.BASE_URL}/madlibs/', headers=self.auth_header) as request:
            ret = await request.json()
            return Madlib(ret['title'], ret['text'], ret['questions'], ret['variables'])

    async def close(self) -> None:
        "Close the client"
        self.session.close()
