#1 link: https://www.codewars.com/kata/576b93db1129fcf2200001e6

def sum_array(array):
    if array == None or len(array) < 3:
        return 0

    array.remove(max(array))
    array.remove(min(array))

    return sum(array)

#2 link: https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

#3 link: https://www.codewars.com/kata/58ca658cc0d6401f2700045f

def find_multiples(n, limit):
    num = []
    num1 = n
    while num1 <= limit:
        num.append(num1)
        num1 += n
    return num

#4 link: https://www.codewars.com/kata/50ee6b0bdeab583673000025/train/python

a = "code"
b = "wa.rs"
name = a + b

#5 link: https://www.codewars.com/kata/55c28f7304e3eaebef0000da/train/python

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res

#6 link: https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python

def make_negative( number ):
    if number <= 0:
        return number
    else:
        return -number

#7 link: https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    result = ""
    for i in dna:
        if i == "A":
            result += "T"
        elif i == "T":
            result += "A"
        elif i == "C":
            result += "G"
        elif i == "G":
            result += "C"
    return result

#8 link: https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

def century(year):
    return (year - 1) // 100 + 1