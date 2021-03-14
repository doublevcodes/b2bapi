class Madlib:

    def __init__(self, title, text, number_of_questions, questions) -> None:
        self.title = title
        self.text = text
        self.number_of_questions = number_of_questions
        self.questions = questions
        self.responses = ()

    def __iter__(self) -> iter:
        return iter(self.questions)

    def __str__(self):
        return self.text

    def get_responses(self) -> tuple:
        ret = []
        for question in self:
            print(f'Please enter a/an {question}')
            ret.append(input())
        self.responses = tuple(ret)
        return tuple(ret)

    def substitute(self) -> str:
        self.text = self.text.format(*self.responses)
        return self.text
