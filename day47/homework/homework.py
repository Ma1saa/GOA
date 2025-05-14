#1. Write a function that takes three numbers and returns the largest one without using max().


def max_num(n, u, m):
    if n > u and n > m:
        return n
    elif u > m and u > n:
        return u
    elif m > n and m > u:
        return m


#2. Create a function that counts how many vowels are in a word, ignoring case.


def vowel_counter(n):
    vowels = 0
    for i in n:
        if i in 'aeiou':
            vowels += 1

    return vowels


#3. Create a function that checks if a word is a palindrome. A palindrome is a word that reads the same forward and backward, like 'racecar' or 'level', ignoring capitalization.


def palindrome_check(n):
    if n == n[::-1]:
        return "palindrome"


#4. Write a function that reverses a given string.


def string_reverse(n):
    return n[::-1]


#5. Create a function that finds the longest word in a sentence. (მოიძიეთ ინფრომაცია split()-ზე.


def long_word_founder(n):
    p = n.split()
    l = len(n)



