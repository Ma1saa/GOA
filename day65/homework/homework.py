#1
def check_age(age):
    if age < 0:
        raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი")
    return f"ასაკი არის: {age}"

#2
def check_word(word):
    if not word:
        raise ValueError("სიტყვა არ უნდა იყოს ცარიელი")
    return f"შეყვანილი სიტყვა: {word}"

#3
add = lambda a, b: a + b

#4
c_to_f = lambda c: (c * 9/5) + 32

for c in range(0, 10):
    print(f"{c}°C = {c_to_f(c)}°F")

#5
nums = [3, 6, 9, 12, 15]
print(list(map(lambda x: x + 5, nums)))

#6
words = ['hello', 'world', 'python']
print(list(map(lambda x: x.upper(), words)))

#7
nums1 = [5, 8, 11, 14, 17]
print(list(filter(lambda x: x > 10, nums1)))

#8
words = ['ant', 'elephant', 'dog', 'giraffe']
print(list(filter(lambda x: len(x) >= 5, words)))

#9
nums2 = [2, 4, 6, 8]
print(list(map(lambda x: x * 2, nums2)))

#10
nums3 = [1, 2, 3, 4, 5, 6]
filtered = list(filter(lambda x: x % 2 == 0, nums3))
print(list(map(lambda x: x + 10, filtered)))
