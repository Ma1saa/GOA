#1
name = "mate"


def speller(name):
    for letter in name[::-1]:
        print(letter)


speller(name)


#2
def numb_list(num1, num2, num3, num4, num5):
    num_list = [num1, num2, num3, num4, num5]
    return num_list


print(numb_list(int(input("enter a number: ")),
                int(input("enter a number: ")),
                int(input("enter a number: ")),
                int(input("enter a number: ")),
                int(input("enter a number: "))))


#3
numbers_list = [69, 420, 5, 9, 400]


def list_scanner(numbers_list):
    max_number = (max(numbers_list))
    min_number = (min(numbers_list))
    sum_of_numbers = sum(numbers_list)
    length = len(numbers_list)
    return print(f"max number is {max_number}, min number is {min_number}, sum of the numbers is {sum_of_numbers}, and lenght is {length}")


print(list_scanner(numbers_list))
