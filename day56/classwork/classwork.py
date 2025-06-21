#1 link: https://www.codewars.com/kata/5672a98bdbdd995fad00000f

def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return  "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "paper":
        return "Draw!"
    elif p1 == "rock" and p2 == "rock":
        return "Draw!"
    elif p1 == "scissors" and p2 == "scissors":
        return "Draw!"
    elif p1 == "rock" and p2 == "paper":
        return  "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return  "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return  "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return  "Player 1 won!"


#2 link: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrev_name(name):
    name2 = name.split(" ")
    first = name2[0]
    last = name2[1]

    return first[0].upper() + "." + last[0].upper()