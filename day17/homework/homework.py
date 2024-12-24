#1
user_age = int(input("Enter your age: "))
friend_age = int(input("Enter your friend's age: "))
if user_age > friend_age:
    print("You are older than your friend.")
elif user_age < friend_age:
    print("You are younger than your friend.")
else:
    print("You and your friend are the same age.")
#2
birth_year = int(input("Enter your year of birth: "))
if birth_year > 2010:
    print("You are a representative of Generation Alpha.")
#3
age = int(input("Enter your age: "))
if age > 10:
    future_age = age + 15
    print(f"In 15 years, you will be {future_age} years old.")
else:
    past_age = age - 5
    print(f"Five years ago, you were {past_age} years old.")
#4
years_to_travel = int(input("How many years do you want to travel forward in time? "))
birth_year = int(input("Enter your year of birth: "))

current_year = 2024
current_age = current_year - birth_year

future_age = current_age + years_to_travel
print(f"In {years_to_travel} years, you will be {future_age} years old.")

#5
#for loop-ს იმ დროს იყენებ როცა იცი რამდენჯერ გინდა რამის
#გამეორება.
#while loop-ი გამოიყენება მაშინ როცა არ იცი რამდენჯერ უნდა გაიმეორო
#რაღაცა სანამ სწორია რაც შიგნია

