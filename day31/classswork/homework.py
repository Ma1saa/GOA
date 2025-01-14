def addition(x,y):
    return x + y


result = addition(4,2)
print(result)


def subtraction(x,y):
    print(x-y)


subtraction(4,2)


def fiveElementList():
    elements = ["milk", "water", "banana", "apple", "soda"]
    sicret_index = 4
    print(elements)
    user_choice = input("choose the element from the list")

    if user_choice in elements and user_choice != "soda":
        print('wrong')
    else: print("you win")


fiveElementList()





