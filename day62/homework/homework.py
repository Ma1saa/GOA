#1
from day56.homework.homework import student


def tuple_info(my_tuple):
    print(f"The tuple has {len(my_tuple)} elements.")
    print(f"First element: {my_tuple[0]}")
    print(f"Last element: {my_tuple[-1]}")

#2
person = ("Giorgi", 25, "Georgia")

name, age, country = person

print("Name:", name)
print("Age:", age)
print("Country:", country)

#3
list1 = [1, 2, 3, 4]

tuple1 = tuple(list1)

list2 = list(tuple1)

print("Original list:", list1)
print("Converted to tuple:", tuple1)
print("Converted back to list:", list2)

#4
numbers = {1, 2, 3, 4, 5}

numbers.add(11)
numbers.add(10)

numbers.remove(1)
numbers.remove(2)


even_numbers = {2, 4, 6, 8, 10}

print(numbers.union(even_numbers)) # აერთიანებს ყველა უნიკალურ ელემენტებს ორი set-იდან
print(numbers.intersection(even_numbers)) # ართიანებს ყველა იგივე ელემენტს
print(numbers.difference(even_numbers)) # აჩვენებს მხოლოდ იმ ელემენტებს რომელიც პირველ set-შია და არა მეორე set-ში


#5
def set_add_remove(my_set):
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    my_set.remove(4)
    return my_set

#6
student1 = {
    "name": "Giorgi",
    "age": 25,
    "height": 180,
    "weight": 80,
    "country": "Georgia",
    "hobby": "reading"
}

print(student1.get("name"))
student1.pop("height")

#7
def dictionary_keys_values(my_dict):
    return my_dict.keys(), my_dict.values()

#8
person = {
    "name": "Giorgi",
    "age": 25,
    "country": "Georgia"
}

for key, value in person.items():
    print(f"{key}: {value}")

#9
animal = {
    "name": "dog",
    "age": 5,
    "country": "Germany"
}

animal_copy = animal.copy()

animal.clear()
animal_copy.clear()

print(animal)
print(animal_copy)

#10
def dictionary_add_pop(my_dict1):
    my_dict1["age"] = 14
    my_dict1.popitem()
    return my_dict1

