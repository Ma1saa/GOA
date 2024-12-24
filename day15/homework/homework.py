#1
def check_number(num):
  if num > 0:
    print("The number is positive.")
  elif num < 0:
    print("The number is negative.")
  else:
    print("The number is zero.")

number = float(input("Enter a number: "))
check_number(number)

#2
age = int(input("Enter your age: "))
if age >= 18:
    print("You are allowed to vote.")
else:
    print("You are not allowed to vote.")

#3
while True:
    score = int(input("Enter your score:"))
    if 100 >= score >= 50:
        print("Congrats you passed!")
        break
    elif 0 <= score < 50:
        print("You failed.")
        break
    else:
        print("invalid score.")
        break
#4
while True:
    user_number = int(input("Enter a number: "))
    if user_number <= 10:
        print("pick higher number")
    else:
        print("task completed")
        break
#5
user_1num = int(input("Enter a number: "))
user_2num = int(input("Enter another number: "))
if user_1num == user_2num:
    print("they are equal")
elif user_1num > user_2num:
    print("first number is greater than second number")
else:
    print("second number is greater than first number")

