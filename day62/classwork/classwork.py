person1 = ('mate', 'maisuradze', 15, 'georgian')

name, surname, age, country = person1


NUM1 = {1, 2, 3, 4, 5, 6, 7}
NUM2 = {4, 5, 6, 7, 8, 9, 10}

NUM1.add(11)
NUM1.remove(7)

NUM2.remove(4)
NUM2.add(11)

print(NUM1.union(NUM2))
print(NUM1.intersection(NUM2))
print(NUM1.difference(NUM2))


person = {
    'name': 'mate',
    'surname': 'maisuradze',
    'age': 15,
    'country': 'georgian',
    'sport': 'football',
    'hobby': 'reading'
}

print(person['name'])

person['city'] = 'kampala'

person['pet'] = 'dog'

print(person.values())
print(person.keys())
print(person.items())

person2 = person.copy()


person2.update({
    'age': 16,
    'city': 'berlin'
})

person.pop('pet')
person.popitem()
person.get('age')

print(person)
print(person2)