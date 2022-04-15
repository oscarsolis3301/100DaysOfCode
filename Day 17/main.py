from question_model import Questions
from data import question_data
import random


question_bank = []
for data in question_data:
    question = Questions(data["text"], data["answer"])
    question_bank.append(question.text)

print(random.choice(question_bank))


