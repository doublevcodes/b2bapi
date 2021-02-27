import json

class Madlib:
    json_decoder = json.loads

    def __init__(self, Json: str) -> None:
        ret = self.json_decoder(Json)
        self.title = ret["title"]
        self.text  = ret["text"]
        self.number_of_questions = ret['questions']
        self.questions = ret['variables']

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
