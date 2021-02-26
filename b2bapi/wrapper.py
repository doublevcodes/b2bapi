import requests
from endpoints.meme import Meme
from endpoints.madlibs import Madlibs
from endpoints.word import Word
from endpoints.speedtext2 import Speedtext

class BytesToBits:

    def __init__(self) -> None:
        self.base_url = 'https://api.bytestobits.dev'
        return

    def get_word(self) -> str:
        ret = requests.get(f'{self.base_url}/word/').json()
        ret = Word(ret)
        return ret

    def get_speedtext(self) -> str:
        ret = requests.get(f'{self.base_url}/speedtext2/').json()
        ret = Speedtext(ret)
        return ret

    def get_meme(self) -> Meme:
        ret = requests.get(f'{self.base_url}/meme/').json()
        ret = Meme(ret['title'], ret['url'], ret['link'], ret['subreddit'])
        return ret

    def get_madlib(self) -> Madlibs:
        ret = requests.get(f'{self.base_url}/madlibs/').json()
        ret = Madlibs(ret['title'], ret['text'], ret['questions'], ret['variables'])
        return ret