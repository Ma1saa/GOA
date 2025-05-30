<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ef0b3482af47208a82657981309c43eb1c15048f
#1 link: https://www.codewars.com/kata/5a00e05cc374cb34d100000d
from day31.homework.homework import string


def reverse_seq(n):
    if n > 0:
        return list(range(n, 0, -1))
    else:
        return []

#2 link: https://www.codewars.com/kata/5545f109004975ea66000086

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False

#3 link: https://www.codewars.com/kata/55cbd4ba903825f7970000f5

def get_grade(s1, s2, s3):
    if 90<=(s1 + s2 + s3)/3<=100:
        return 'A'
    elif 80<=(s1 + s2 + s3)/3<90:
        return 'B'
    elif 70<=(s1 + s2 + s3)/3<80:
        return 'C'
    elif 60<=(s1 + s2 + s3)/3<70:
        return 'D'
    elif 0<=(s1 + s2 + s3)/3<60:
        return 'F'

#4 link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
    for i in l[:]:
        if i == str(i):
            l.remove(i)
    return l

#5 link: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(n):
    n = n.split()
    min_len = len(n[0])
    for i in n:
        if len(i) < min_len:
            min_len = len(i)
<<<<<<< HEAD
=======
=======
#1 link: https://www.codewars.com/kata/5a00e05cc374cb34d100000d
from day31.homework.homework import string


def reverse_seq(n):
    if n > 0:
        return list(range(n, 0, -1))
    else:
        return []

#2 link: https://www.codewars.com/kata/5545f109004975ea66000086

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False

#3 link: https://www.codewars.com/kata/55cbd4ba903825f7970000f5

def get_grade(s1, s2, s3):
    if 90<=(s1 + s2 + s3)/3<=100:
        return 'A'
    elif 80<=(s1 + s2 + s3)/3<90:
        return 'B'
    elif 70<=(s1 + s2 + s3)/3<80:
        return 'C'
    elif 60<=(s1 + s2 + s3)/3<70:
        return 'D'
    elif 0<=(s1 + s2 + s3)/3<60:
        return 'F'

#4 link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
    for i in l[:]:
        if i == str(i):
            l.remove(i)
    return l

#5 link: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(n):
    n = n.split()
    min_len = len(n[0])
    for i in n:
        if len(i) < min_len:
            min_len = len(i)
>>>>>>> 1eeb71ee1b8b1111caeb3112674d41aee1115043
>>>>>>> ef0b3482af47208a82657981309c43eb1c15048f
    return min_len