# In this program, we will be calculating how much each person will need to pay
# taking into account how many people there are and a tip percentage

print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = (tip / 100) * total
total += tip
total /= people
total = round(total, 1)

print(f"Each person should pay: ${total}")
