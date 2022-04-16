class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list

    def still_has_q(self):
        return self.q_number != len(self.q_list)

    def question(self):
        q_question = self.q_list[self.q_number]
        self.q_number += 1
        u_answer = input(f"Q.{self.q_number}: {q_question.text} (true/false): ")
        self.check_answer(u_answer, q_question)

    def check_answer(self, u_answer, q_question):
        if u_answer.lower() == q_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That was incorrect.")
        print(f"The correct answer was: {q_question.answer}.")
        print(f"Your current score is: {self.score}/{self.q_number}")
        print("\n")