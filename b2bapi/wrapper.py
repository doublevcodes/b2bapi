import requests
from time import sleep
from madlibs import Madlib

class Meme:
    def __init__(self, title: str, url: str, link: str, subreddit: str) -> None:
        self.title = title
        self.url = url
        self.link = link
        self.subreddit = subreddit

    def __str__(self):
        return self.title


class Word:
    
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word

class Speedtext:
    
    def __init__(self, text) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text

    def __repr__(self):
        return self.text

    def typewriter(self):
        for char in self.text:
            print(char, end='', flush=True)
            sleep(0.08)

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

    def get_madlib(self) -> Madlib:
        ret = requests.get(f'{self.base_url}/madlibs/').json()
        ret = Madlib(ret['title'], ret['text'], ret['questions'], ret['variables'])
        return ret