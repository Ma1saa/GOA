numbers1 = [1, 2, 3, 4, 5,]
numbers2 = [69, 55, 420, 33, 44]
numbers3 = [66, 12, 81, 96, 79]
print(max(numbers1), max(numbers2), max(numbers3))


print(min(numbers1), min(numbers2), min(numbers3))


print(len(numbers1), len(numbers2), len(numbers3))


list1 = ["cat", "dog", "lion", "tiger", "elephant", "wolf", "fox", "bear", "rabbit", "zebra"]
list2 = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"]
list3 = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "white", "black", "gray"]
list4 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
print(list1[:4])
for i in list2[3:8]:
    print(i)

print(list3[-2:-6:-1])


while True:
    print(list4)
    break


num_list = [int(input("enter a number")),
            int(input("enter a number")),
            int(input("enter a number")),
            int(input("enter a number")),
            int(input("enter a number")),]


def list_scanner_3000(num_list):
    print(min(num_list))
    print(max(num_list))
    print(sum(num_list))
    print(len(num_list))


print(list_scanner_3000(num_list))

