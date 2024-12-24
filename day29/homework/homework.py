
def bmi(height, weight):
    bmi = weight / height**2
    if bmi < 18.5:
        print('Underweight')
    elif bmi >= 18.5 and bmi < 24.9:
        print('Normal')
    elif bmi >= 25 and bmi < 29.9:
        print('Overweight')
    elif bmi >= 30 and bmi < 34.9:
        print('Obese')
    elif bmi >= 35:
        print('extremely Obese')


bmi(float(input('Enter your height: ')), int(input('Enter your weight: ')))


def threeproduct(num1, num2, num3):
    print(num1 * num2 * num3)


threeproduct(6, 7, 8)


def greet(name):
    print("hello", name)


greet(input( "enter your name" ))


def comparison(num1, num2):
    print(num1 == num2)
    print(num1 < num2)
    print(num1 <= num2)
    print(num1 >= num2)
    print(num1 > num2)


comparison(6, 7)


def agecalc(age):
    print(2024 - age)


agecalc(int(input('Enter your age:')))
