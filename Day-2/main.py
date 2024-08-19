# print(round(8/3)) 
# print(round(8/3 ,2))
# print(round(8/4 ,3))

# score=10
# height=180
# win = True
# print(f"score = {score}, height = {height}, win = {win}")

print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
total = bill + (bill*(tip/100))
per = round(total/split, 2)
per = "{:.2f}".format(per)

print(f"Each person should pay: ${per}")