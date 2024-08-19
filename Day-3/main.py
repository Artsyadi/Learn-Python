print("Welcome to the rollercoster")
height = int(input("What is your height in cm? "))
age = int(input("Enter age: "))
bill = 0

"""
if height >= 120:
    print("You can ride rollercoster")
else:
    print("sorry tou cannot")
"""

"""
if height >= 120:
    print("You can ride rollercoster")
    if age <12:
        print("Pay 7$")
    else:
        print("Pay 12$")
else:
    print("sorry tou cannot")
"""
"""
if height >= 120:
    print("You can ride rollercoster")
    if age <12:
        print("Pay 7$")
    elif age<=18:
        print("Pay 10$")
    else:
        print("Pay 12$")
else:
    print("sorry you cannot")
"""
#BMI Calculator
"""
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

bmi = weight/height**2
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi>=18.5 and bmi<25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi>=25 and bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>=30 and bmi<35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically overweight.")
"""
#Leap Year Calculator
"""
# Which year do you want to check?
year = int(input())

if year %4 ==0:
  if year%100 ==0:
    if year%400==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
"""
#roller Coaster
"""
if height >= 120:
    print("You can ride rollercoster")
    if age <12:
        bill=7
        print("Pay 7$")
    elif age<=18:
        bill=10
        print("Pay 10$")
    else:
        bill=12
        print("Pay 12$")

    photo = input("Do you want photo? Y or N. ")
    if photo=="Y":
        bill+=3
    print(f"Yor total is {bill}")
else:
    print("sorry you cannot")
"""
#Pizza Express
"""
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
"""
#Love calculator
"""
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  """