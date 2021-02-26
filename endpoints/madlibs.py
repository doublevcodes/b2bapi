class Madlibs:

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
    
    def substitute(self, responses) -> str:
        self.text = self.text.format(*responses)
        return self.text
