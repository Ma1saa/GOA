name = "mate"
print(name[1])


num1 = 10
num2 = 20
print(num1 + num2)


# კონკატენაცია ნიშნავს ორი სტრინგის შეერთება ერთად.
str1 = "Hello, "
str2 = "World!"
print(str1 + str2)


num3 = 5
num4 = 2
result = num3 / num4
print(result)
# გამომავალი არის float-ი რადგან პითონი ასრულებს იმპლიციტურ კონვერტაციას გაყოფის დროს.


print(5 == 5)
print(5 != 3)
print(5 < 6)
print(7 > 4)
print(4 <= 4)
print(8 >= 9)


print(5 + 5 == 8 + 2)
print(10 - 2 > 3 * 2)


a, b = True, False
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)


print(5 > 3 and 2 < 4)
print(10 == 10 or 5 > 8)
print(69 < 420 and 5 < 2)
print((8 > 5) and (3 < 7))
print((10 < 5) or (6 == 6))


for i in range(1, 11):
    print(i)


numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)


for char in "Hello, World!":
    print(char)


i = 1
while i <= 10:
    print(i)
    i += 1


i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1


sum_numbers = 0
i = 1
while sum_numbers < 50:
    sum_numbers += i
    i += 1
print(sum_numbers)
