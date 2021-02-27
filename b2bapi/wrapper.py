import requests
from time import sleep

class Meme:
    def __init__(self, title: str, url: str, link: str, subreddit: str) -> None:
        self.title = title
        self.url = url
        self.link = link
        self.subreddit = subreddit

    def __str__(self):
        return self.title

class Madlib:

    def __init__(self, title: str, text: str, number_of_questions: int, questions: list) -> None:
        self.title = title
        self.text  = text
        self.number_of_questions = number_of_questions
        self.questions = questions

    def __iter__(self) -> iter:
        return iter(self.questions)

    def __str__(self):
        return self.text

    def get_responses(self) -> tuple:
        ret = []
        for question in self:
            print(f'Please enter a/an {question}')
            ret.append(input())
        self.responses = ret
        return tuple(ret)
    
    def substitute(self) -> str:
        self.text = self.text.format(*self.responses)
        return self.text

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