def greetings(special, *guests, **visitors):
    print('welcome' + special)
    for guest in guests:
        print("helo" + guest)

    for kay, value in visitors:
        print(kay + ":" + value)


greetings("special", "john", "jane", "jim", jack="123", jill="456")


def decorator(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

def greet(name):
    print(f"Hello, {name}!")

greet = decorator(greet)
greet("Alice")

@decorator
def greet2(name):
    print(f"Hi, {name}!")

greet2("Bob")
