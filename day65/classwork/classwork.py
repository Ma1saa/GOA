def add_numbers(num1, num2):
    return num1 + num2

def full_name(first_name, last_name):
    return first_name + " " + last_name

print(add_numbers(10, 20))
print(add_numbers(3, 1))
print(full_name("Mate", "Maisuradze"))
print(full_name("John", "Doe"))


print(lambda num1, num2: num1 + num2)
print(lambda first_name, last_name: first_name + " " + last_name)


def manual_map(func, list):
    result = []
    for item in list:
        result.append(func(item))
    return result

def manual_filter(func, list):
    result = []
    for item in list:
        if func(item):
            result.append(item)
    return result

