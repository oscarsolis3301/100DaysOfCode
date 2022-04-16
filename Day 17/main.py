from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_list = []
for data in question_data:
    new_question = Question(data["question"], data["correct_answer"])
    question_list.append(new_question)
quiz = QuizBrain(question_list)

while quiz.still_has_q():
    quiz.question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_list)}")