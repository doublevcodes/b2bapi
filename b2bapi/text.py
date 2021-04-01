from time import sleep


class Text:

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
