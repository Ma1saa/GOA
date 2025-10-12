#1
def sum_of_numbers(*args):
    return sum(args)

#2
def string_concatenation(*args):
    return "".join(args)
#3
def print_info(**kwargs):
    print(f"name: {kwargs['name']}, age: {kwargs['age']}")

#4
def print_car_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#5
def decorator(func):
    def wrapper():
        print("ფუნქცია დაიწყო")
        func()
        print("ფუნქცია დასრულდა")
    return wrapper

@decorator
def greet():
    print("გამარჯობა!")

greet()

#6
