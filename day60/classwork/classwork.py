#1 link: https://www.codewars.com/kata/515e271a311df0350d00000f

def square_sum(numbers):
    sum_nums = 0

    for nums in numbers:
        sum_nums += nums ** 2
    return sum_nums

#2 link: https://www.codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    string = ''
    for i in x:
        if int(i) < 5:
            string += '0'
        else:
            string += '1'
    return string

#3 link: https://www.codewars.com/kata/551b4501ac0447318f0009cd

def boolean_to_string(b):
    if b == True:
        return 'True'
    else:
        return 'False'

#4 link: https://www.codewars.com/kata/56b1f01c247c01db92000076

def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result

