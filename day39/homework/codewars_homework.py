#1 link: https://www.codewars.com/kata/544675c6f971f7399a000e79
def string_to_number(s):
    return int(s)


#2 link: https://www.codewars.com/kata/50654ddff44f800200000004
def multiply(a, b):
    return a * b


#3 link: https://www.codewars.com/kata/53369039d7ab3ac506000467
def bool_to_word(boolean):
    if boolean == True:
        return "yes"
    elif boolean == False:
        return "no"

#4 link: https://www.codewars.com/kata/55ca77fa094a2af31f00002a

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


#5 link: https://www.codewars.com/kata/5715eaedb436cf5606000381
arr = [5, 9, 69, -2, -88]
def positive_sum(arr):
    total = 0
    for i in arr:
        if i > 0:
            total += i
    return total
