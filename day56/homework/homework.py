#1

def list_multiplier(list1):
    list2 = []
    for i in list1:
        list2.append(i*2)

    return list2

#2

num1 = input("enter first number ")
num2 = input("enter second number ")
num3 = input("enter third number ")
num4 = input("enter fourth number ")
num5 = input("enter fifth number ")

list = [num1, num2, num3, num4, num5]

print(list)

#3

def words_length(words):
    length = []
    for i in words:
        length.append(len(i))

    return length

#4

students = []

while True:
    name = input("Enter your name (or 'done' to finish): ")
    if name.lower() == 'done':
        break

    grade1 = float(input("Enter first grade: "))
    grade2 = float(input("Enter second grade: "))
    grade3 = float(input("Enter third grade: "))

    average = (grade1 + grade2 + grade3) / 3
    students.append((name, average))

print("Student Averages:")
for student in students:
    print(student[0], "-", "Average:", student[1])

#5

def filter_long_strings(strings):
    result = []
    for s in strings:
        if len(s) > 3:
            result.append(s)
    return result

