#1 link: https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python
def make_upper_case(s):
    s = s.upper()
    return s


#2 link: https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
def string_to_number(s):
    return int(s)


#3 link: https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
def is_uppercase(inp):
    if inp == inp.upper():
        return True
    else:
        return False


#4 link: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    m = []
    n = str(n)
    for i in n[::-1]:
        m.append(int(i))
    return m
