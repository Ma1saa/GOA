age = int(input("Enter your age: "))
if age >= 18:
    print("You are a adult")
else:
    print("You are a child")


password = "super_sicret_parol"
guess = input("Guess a password: ")
if password == guess:
    print("You are correct")
else:
    print("You are incorrect password is " + " " + password)

