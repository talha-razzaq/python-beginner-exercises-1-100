# 🟡 4. if / elif / else — Exercises 21–35

#🔴21. Positive or Negative-Determine whether a number is positive, negative, or zero.
num = int(input("Enter the number: "))
if num > 0:
    print(f"{num} is positive digit.")
elif num < 0:
    print(f"{num} is negetive digit.")
else:
    print(f"{num} is zero digit.")

#🔴 22. Even or Odd-Determine whether a number is even or odd.
numb = int(input("Enter the number: "))
if numb % 2 == 0:
    print(f"{numb} is an even number.")
else:
    print(f"{numb} is an odd number.")

#🔴 23. Greater Number-Take two numbers and print the greater one.
num1 = int(input("Enter the number-1: "))
num2 = int(input("Enter the number-2: "))

if num1 > num2:
    print(f"{num1} is greater digit.")
elif num2 > num1:
    print(f"{num2} is greater digit.")
else:
    print("Both digits are equal.")

#🔴 24. Largest of Three-Find the largest of three numbers.
number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))
number3 = int(input("Enter the number3: "))

if number1 >= number2 and number1 >= number3:
    print(f"{number1} is the greater than other two digits.")
elif number2 >= number1 and number2 >= number3:
    print(f"{number2} is the greater than other two digits.")
else:
    print(f"{number3} is the greater than other two digits.")

#🔴 25. Smallest of Three-Find the smallest of three numbers.

number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
number3 = int(input("Enter the number 3: "))

if number1 <= number2 and number1 <= number3:
    print(f"{number1} is the smallest number.")
elif number2 <= number1 and number2 <= number3:
    print(f"{number2} is the smallest number.")
else:
    print(f"{number3} is the smallest number.")

#🔴 26. Pass or Fail-Take marks and determine whether the student passed.
marks = int(input("Enter the number : "))
if marks >= 50:
    print("You passed")
else:
    print("You failed")
#🔴 27. Grade Calculator-Create grades such as:
# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F
obt_marks = int(input("Enter the marks: "))
if obt_marks >= 90:
    print("Grade A.")
elif obt_marks >= 80:
    print("Grade B")
elif obt_marks >= 70:
    print("Grade C")
elif obt_marks >= 60:
    print("Grade D")
else:
    print("You failed.")

#🔴 28. Voting Eligibility-Ask for age and determine whether someone can vote.
voter_age = int(input("Enter the number: "))
if voter_age >= 18:
    print("You can vote.")
else:
    print("You can't vote.")

#🔴 29. Driving Eligibility-Check whether a person is old enough to drive.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

#🔴 30. Number Divisibility-Check whether a number is divisible by 5.
num_check = int(input("Enter the number: "))
if num_check % 5 == 0:
    print(f"{num_check} is divisible by 5.")
else:
    print(f"{num_check} is not divisible by 5.")

# 🔴 31. Divisible by 3 and 5-Check whether a number is divisible by both 3 and 5.
number_check = int(input("Enter the number: "))
if number_check % 5 == 0 and number_check % 3 == 0:
    print(f"{number_check} is divisible by 5 and 3.")
else:
    print(f"{number_check} is not divisible by 5 and 3.")

# 🔴 32. Leap Year-Determine whether a year is a leap year.
year = int(input("Enter your leap year: "))

if year % 400 == 0:
    print("Its leap year.")
elif year % 100 == 0:
    print("Its not leap year.")
elif year % 4 == 0:
    print("Its leap year.")
else:
    print("Its not a leap year.")
# 🔴 33. Temperature
# Classify temperature as:
# Cold
# Normal
# Hot
# Very Hot
weather = int(input("Enter the temperture: "))
if weather <= 15:
    print("Its cold outside.")
elif weather <= 25:
    print("Todays is good and normal temperture.")
elif weather <= 40:
    print("It's hot outside.")
else:
    print("Its too hot outside.")
# 🔴 34. Simple Login
# Ask for username and password and check whether they are correct.
user_name = input("Enter the user name: ")
pwd = int(input("Enter the password: "))

if user_name == "talha" and pwd == 123:
    print("Login in Lms.")

else:
    print("You can't login.")

# 🔴 35. Simple Calculator
# Ask for two numbers and an operator:
# +
# -
# *
# /

number1 = int(input("Enter the number 1 : "))
number2 = int(input("Enter the number 2 : "))

calculation = input("Enter the your calculation +, -, *, / : ")

if calculation == "+":
    addition = number1 + number2
    print(f"The addition {number1} and {number2} is {addition} ")
elif calculation == "-":
    minus = number1 - number2
    print(f"The minus {number1} and {number2} is {minus} ")
elif calculation == "*":
    multiply = number1 * number2
    print(f"The multiply {number1} and {number2} is {multiply} ")
elif calculation == "/":
    if number2 != 0:
        division = number1 / number2
        print(f"The division of {number1} and {number2} is {division}.")
    else:
        print("You cannot divide by zero.")

else:
    print("Invalid operator.")