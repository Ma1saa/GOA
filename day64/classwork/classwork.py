input(enter your name) #SyntaxError

print(5 + "10") #TypeError

names = ["John", "Eric", "Michael"]
int(names) #ValueError

print(69 / 0) #ZeroDivisonError

try:
    name = 'mate'
    print(name[1]) #IndexError
except IndexError:
    print('IndexError')

print(sername) #nameerror


products = ['soda', 'chocolate', 'gum', 'chips', 'water', 'energy drink']
try:
    inpt = int(input('enter a index of a product: '))
except ValueError:
    print('enter a valid index')
    inpt = int(input('enter a index of a product: '))

if inpt > 3:
    raise IndexError()