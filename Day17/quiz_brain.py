class Brain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            print("RIGHT!")
            self.score += 1
        else:
            print("WRONG!")
        print(f"Current score is: {self.score}/{self.question_number}")
        print(f"The correct answer was: {right_answer}.")
