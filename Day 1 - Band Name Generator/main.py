# In this program, we will be creating a band name from the city that the user grew up in and a pet name

print('Welcome to the Band Name generator.')

city = input("What's the name of the city you grew up in?\n")

pet = input("What's your pet's name?\n")

band = city + " " + pet

print(f"Your band name could be {band}")