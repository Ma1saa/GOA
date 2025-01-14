#1
num1 = int(input("Enter a number: "))


def addition():
    print(num1+5)


addition()

#2
def multiplication(x, y):
    print(x*y)


multiplication(int(input("Enter a number: ")), int(input("Enter a number: ")))

#3
string = input("Enter a string: ")


def strings_length():
    print(len(string))


strings_length()

#4
shopping_list = ["apple", "banana", "cherry"]


def lists_length():
    print(len(shopping_list))


lists_length()

#5
user_input = input("Enter a word: ")


def palindrome(user_input):
    if user_input == user_input[::-1]:
        return print(True)
    else:
        return print(False)


palindrome(user_input)


#6
user_input2 = input("Enter a word: ")


def uppercase():
    print(user_input2.upper())


uppercase()
