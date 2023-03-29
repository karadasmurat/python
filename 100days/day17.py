import json
import random
from typing import List

import deprecated
# import from a source file in a subfolder:
from data.questions import question_data


class Score:
    def __init__(self):
        self.total_score = 0
        self.correct_count = 0
        self.incorrect_count = 0

    def increment_correct(self):
        self.correct_count += 1
        self.total_score += 10  # assume each correct is 10 points

    def increment_incorrect(self):
        self.incorrect_count += 1

    def calculate_percentage(self):
        if self.total_score == 0:
            return 0
        else:
            return (self.correct_count / self.total_score) * 100

    def __str__(self):
        return f"{self.correct_count} / {self.correct_count + self.incorrect_count}"


class Question:

    def __init__(self, text: str, options: List[str], answer: str):
        self.text = text
        self.options = options
        self.answer = answer

    def question_text_with_options(self, shuffled: bool = False):
        '''
        Print the question and options. Options can be shuffled based on shuffled arg.
        :param shuffled: Whether to suffle the options
        '''
        q_str = self.text + "\n"
        if shuffled:
            # options = random.sample(self.options, len(self.options))
            random.shuffle(self.options)    # shuffle in place, and return None

        for i, option in enumerate(self.options):
            q_str += f"{chr(65+i)}. {option}\n"

        return q_str

    def check_answer(self, label):
        # print("answer index:", ord(label)-65)
        return self.options[ord(label)-65] == self.answer  # directly return the condition

    def __repr__(self):
        return f"Question(text={self.text!r}, options={self.options}, answer={self.answer!r})"

    def __str__(self) -> str:
        return self.question_text_with_options()


class QuestionBank:

    def __init__(self, questions: List[Question]):
        # print("QuestionBank: construct object")
        self.questions = questions
        self.currentQuestionIndex = 0
        self.score = Score()

    def nextQuestion(self):
        if self.hasNext():
            question = self.questions[self.currentQuestionIndex]
            self.currentQuestionIndex += 1
            return question

    def hasNext(self):
        return self.currentQuestionIndex < len(self.questions)

    def ask(self):

        question = self.nextQuestion()

        print(question.question_text_with_options(shuffled=True))

        answer = input("Your answer (A, B, C, or D): ").upper()

        is_right = question.check_answer(answer)
        if is_right:
            self.score.increment_correct()
            print(f"🌟 Correct")
            print(self.score)

        else:
            self.score.increment_incorrect()
            print(f"❌ Incorrect. The correct answer: ", question.answer)
            print(self.score)


def main():
    print("day 17")

    q_dict = load_questions()
    # print("List of question dictionaries:", questions)

    # Map a list of dict to a list of question objects, use list comprehension:
    questions = [Question(q['text'], q['options'], q['answer']) for q in q_dict]
    question_bank = QuestionBank(questions)
    # print("List of Question objects: ", question_bank)

    # Option 1: the iteration logic is out of Questionbank
    # We are exposing internals of our logic
    # for question in question_bank.questions:
    #     # print(question.print_with_options(shuffled=True))
    #     ask_question(question)

    # Option 2: Iterator logic.
    while (question_bank.hasNext()):
        # q = question_bank.nextQuestion()
        # ask_question(q)
        question_bank.ask()


def load_questions():
    with open("data/questions.json") as file:
        data = json.load(file)  # whole contents of file as a dict type.
    return data['questions']


@deprecated(reason="This method is deprecated. Use QuestionBank.ask() instead.")
def ask_question(question: Question):

    print(question.question_text_with_options(shuffled=True))

    answer = input("Your answer (A, B, C, or D): ").upper()

    is_right = question.check_answer(answer)
    if is_right:
        print("Correct!")

    else:
        print(f"Incorrect. The correct answer: ", question.answer)

    # if shuffled_options[ord(answer)-65] == question['answer']:
    #     print("Correct!")
    #     return True
    # else:
    #     print(f"Incorrect. The correct answer was {question['answer']}.")
    #     return False


if __name__ == "__main__":
    main()
