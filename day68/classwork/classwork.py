#1 link: https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python
def cookie(x):
    if x == str(x):
        return "Who ate the last cookie? It was Zach!"
    elif x == bool(x):
        return "Who ate the last cookie? It was the dog!"
    elif x == float(x) or x == int(x):
        return "Who ate the last cookie? It was Monica!"

#2 link: https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

#3 link: https://www.codewars.com/kata/5899642f6e1b25935d000161/train/python
def merge_arrays(a, b):
    return sorted(set(a + b))

#4 link: https://www.codewars.com/kata/54598d1fcbae2ae05200112c/train/python
def _all(seq, fun):
    return all(fun(x) for x in seq)

#5 link: https://www.codewars.com/kata/57241e0f440cd279b5000829
def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    return sum(range(n, m, n))

#6 link: https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python
def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]

#7 link: https://www.codewars.com/kata/5a023c426975981341000014
def other_angle(a, b):
    return 180 - (a + b)

#8 link: https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
def switch_it_up(number):
    words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return words[number]

#9 link: https://www.codewars.com/kata/5513795bd3fafb56c200049e
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]
