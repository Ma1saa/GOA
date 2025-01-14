# 1
def square(num):
    return num*num


print(square(5))


# 2
def addition(num1, num2):
    return num1+num2


print(addition(6, 9))


# 3
numb_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def list_min_number_finder(numb_list):
    min_num = min(numb_list)
    return min_num


print(list_min_number_finder(numb_list))


# 4
def numb_checker(numb):
    if numb < 0:
        print("Number is negative")
    else:
        print("Number is positive")


numb_checker(int(input("Enter a number: ")))
