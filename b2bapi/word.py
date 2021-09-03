class Word:
    __slots__ = ("word",)

    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word
    
    def __repr__(self) -> str:
        return f"<Word \"{self.word}\">"