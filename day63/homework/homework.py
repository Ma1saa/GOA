#1
numbers = [1, 4, 7, 10, 13, 16, 19]
new_list = []
for number in numbers:
    if number % 2 == 0:
        new_list.append(number*2)

new_list1 = [i*2 for i in numbers if i % 2 == 0]

#2
words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
fiveLetterWords = []
for word in words:
    if len(word) > 5:
        fiveLetterWords.append(word)

fiveLetterWords1 = [word for word in words if len(word) > 5]

#3
nums = list(range(1, 21))
numsSquare = []
for num in nums:
    numsSquare.append(num**2)

#4
mixed = [2, 5, 8, 11, 14, 17, 20]
even = [i for i in mixed if i % 2 == 0]
odd = [i for i in mixed if i % 2 != 0]

#5
animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
animalsFirstLetters = []
for animal in animals:
    animalsFirstLetters.append(animal[0])

animalsFirstLetters1 = [animal[0] for animal in animals]

animalsFirstLetterE = [animal for animal in animals if animal[0] == 'e']
