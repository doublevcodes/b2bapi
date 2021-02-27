import requests
from time import sleep
from madlibs import Madlib
from meme import Meme
from speedtype2 import Speedtext
from word import Word

class BytesToBits:

    def __init__(self) -> None:
        self.base_url = 'https://api.bytestobits.dev'
        return

    def get_word(self) -> Word:
        "Returns a random word from the API"
        ret = requests.get(f'{self.base_url}/word/').json()
        ret = Word(ret)
        return ret

    def get_speedtext(self) -> Speedtext:
        "Returns a random paragraph from the API"
        ret = requests.get(f'{self.base_url}/speedtext2/').json()
        ret = Speedtext(ret)
        return ret

    def get_meme(self) -> Meme:
        "Returns a random meme from a random subreddit through the API"
        ret = requests.get(f'{self.base_url}/meme/').json()
        ret = Meme(ret['title'], ret['url'], ret['link'], ret['subreddit'])
        return ret

    def get_madlib(self) -> Madlib:
        "Returns a randomadlib from the API"
        ret = requests.get(f'{self.base_url}/madlibs/').json()
        ret = Madlib(ret['title'], ret['text'], ret['questions'], ret['variables'])
        return ret