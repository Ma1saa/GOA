#1 link: https://www.codewars.com/kata/523b4ff7adca849afe000035

def greet():
    return "hello world!"


#2 link: https://www.codewars.com/kata/56200d610758762fb0000002

def add_five(num):
    total = num + 5
    return total

#3 link: https://www.codewars.com/kata/55685cd7ad70877c23000102

def make_negative( number ):
    if number <= 0:
        return number
    else:
        return -number

#4 link: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

def find_average(numbers):
    if len(numbers) != 0:
        average = sum(numbers) / len(numbers)
        return average
    else:
        return 0

#5 link: https://www.codewars.com/kata/57089707fe2d01529f00024a

def check_alive(health):
    if health <= 0:
        return False
    else:
        return True

    