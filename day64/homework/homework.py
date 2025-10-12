#1
try:
    print(1/0)
except ZeroDivisionError:
    print('division by zero')

#2
my_list = [5, 10, 15]

try:
    print(my_list[5])
except IndexError:
    print("ინდექსი არასწორია")

#3
try:
    num = int(input("Enter a number: "))
    print("Your number is:", num)
except ValueError:
    print("Please enter numbers only")

#4
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Please enter valid numbers"
    else:
        print("Division completed successfully")
        return result

#5
def check_number(num):
    if num < 0:
        raise ValueError("რიცხვი არ შეიძლება იყოს უარყოფითი")
    return "რიცხვი სწორია"

#6
try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

#7
while True:
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid input, please enter a number")

#8
my_list = [10, "abc", 25, "hello", 3.5, "50"]

result = []
for item in my_list:
    try:
        result.append(float(item))
    except ValueError:
        pass

print(result)

#9
values = ['10', '20', 'hello', '30']

for item in values:
    try:
        num = int(item)
        print("Converted number:", num)
    except ValueError:
        print(f"მონაცემი არ არის რიცხვი: {item}")
