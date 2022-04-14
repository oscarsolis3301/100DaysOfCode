from question_model import Questions
from data import question_data
import random


question_bank = []
for data in question_data:
    question_bank.append(Questions(data["text"], data["answer"]))


print(random.choice(question_bank["text"]))
