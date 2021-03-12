import requests, aiohttp, asyncio
from time import sleep
from .meme import Meme
from .madlib import Madlib
from .text import Text
from .word import Word


class BytesToBits:

    def __init__(self, token: str) -> None:
        self.auth_header = {
            'Authorization': token
        }
        self.BASE_URL = 'https://api.bytestobits.dev'
        return

    def get_word(self) -> Word:
        "Returns a random word from the API"
        return Word(requests.get(f'{self.BASE_URL}/word/', headers=self.auth_header).json())
        

    def get_text(self) -> Text:
        "Returns a random paragraph from the API"
        ret = requests.get(f'{self.BASE_URL}/text/', headers=self.auth_header).json()
        return Text(ret)

    def get_meme(self) -> Meme:
        "Returns a random meme from a random subreddit through the API"
        ret = requests.get(f'{self.BASE_URL}/meme/', headers=self.auth_header).json()
        ret = Meme(ret['title'], ret['url'], ret['link'], ret['subreddit'])
        return ret

    def get_madlib(self) -> Madlib:
        "Returns a random madlib from the API"
        ret = requests.get(f'{self.BASE_URL}/madlibs/', headers=self.auth_header).json()
        return Madlib(ret['title'], ret['text'], ret['questions'], ret['variables'])

class AsynchronousBytesToBits:

    def __init__(self, token: str) -> None:
        self.auth_header = {
            'Authorization': token
        }
        self.BASE_URL = 'https://api.bytestobits.dev'
        return

    async def get_word(self) -> Word:
        "Returns a random word from the API in an asynchronous context"
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.BASE_URL}/word/', headers=self.auth_header) as request:
                return Word(await request.json())
    
    async def get_text(self) -> Text:
        "Returns a random paragraph from the API in an asynchronous context"
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.BASE_URL}/text/', headers=self.auth_header) as request:
                return Text(await request.json())

    async def get_meme(self) -> Meme:
        "Returns a random meme from a random subreddit through the API in an asynchronous context"
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.BASE_URL}/meme/', headers=self.auth_header) as request:
                ret = await request.json()
                return Meme(ret['title'], ret['url'], ret['link'], ret['subreddit'])

    async def get_madlib(self) -> Madlib:
        "Returns a random madlib from the API in an asynchronous context"
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.BASE_URL}/madlibs/', headers=self.auth_header) as request:
                ret = await request.json()
                return Madlib(ret['title'], ret['text'], ret['questions'], ret['variables'])