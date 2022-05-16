#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../../Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as template:
    data = template.read()

invited = []
with open("../../Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    for x in names:
        new_name = x.strip("\n")
        invited.append(new_name)

for i in range(len(invited)):
    with open(f"../../Day 24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{invited[i]}.txt", "w") as\
            finished_letter:
        new_template = data.replace("[name]", f"{invited[i]}")
        finished_letter.write(new_template)
