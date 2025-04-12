print("problem solver website")

user_input1 = (input("which way do you want to solve? normal/ohm's law "))

def ohms_law(input_I, input_U, input_R):
    if input_I == "":
        print(f" I = {int(input_U) / int(input_R)}A")
    elif input_U == "":
        print(f" U = {int(input_I) / int(input_R)}V")
    elif input_R == "":
        print(f" R = {int(input_U) / int(input_I)}Ω")
    else:
        return "Wrong input"



def normal(input_I, input_q, input_t):
    if input_I == "":
        print(f" I = {int(input_q) / int(input_t)}A")
    elif input_q == "":
        print(f" q = {int(input_I) * int(input_t)}K")
    elif input_t == "":
        print(f" I = {int(input_q) / int(input_I)}seconds")
    else:
        return "Wrong input"



if user_input1 == "normal":
    print(normal(input("enter I (if you dont have I than hit enter )"), input("enter q (if you dont have q than hit enter )"), input("enter t in seconds (if you dont have I than hit enter)")))
elif user_input1 == "ohm's law":
    print(ohms_law(input("enter I (if you dont have I than hit enter )"), input("enter U (if you dont have U than hit enter )"), input("enter r (if you dont have r than hit enter)")))
else:
    print("Wrong input")

