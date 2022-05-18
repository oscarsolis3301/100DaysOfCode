# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#
# print(data)

# import csv
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for i in data:
#         if i[1] == 'temp':
#             pass
#         else:
#             temperatures.append(int(i[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data = pandas.read_csv("weather_data.csv")
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

# data = pandas.read_csv("weather_data.csv")
# monday_data = data[data.day == "Monday"]
# temp = int(monday_data.temp)
# temp *= 9/5
# temp += 32
# print(f"Mondays temp in fahrenheit: {temp}")

# squirrel_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # fur_color = squirrel_file["Primary Fur Color"]
# # list_fur = fur_color.to_list
# # print(list_fur)
#
# amount = squirrel_file["Primary Fur Color"].to_dict()
# data = pandas.Series(amount)
# gray = amount.count("Gray")
# print(data)
# gray_squirrels = amount.count("Gray")
# red_squirrels = amount.count("Cinnamon")
# black_squirrels = amount.count("Black")
#
# data = {"Gray": gray_squirrels, "Red": red_squirrels, "Black": black_squirrels}
# squirrels = pandas.Series(data)
# squirrels.to_csv("Squirrels.csv")


sf = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = sf["Primary Fur Color"]
colors_list = colors.to_list()
gray_squirrels = colors_list.count("Gray")
red_squirrels = colors_list.count("Cinnamon")
black_squirrels = colors_list.count("Black")

squirrel_data = {
    "Primary Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(squirrel_data)
df.to_csv("Squirrel_Count.csv")
