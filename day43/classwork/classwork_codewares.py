arr = [1,2,3,4,5,6,7,8,9,10,-3,-5,-1]


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else:
        list = []
        list2 = []
        for i in arr:
            if i > 0:
                list.append(i)
        for i in arr:
            if i < 0:
                list2.append(i)
        return [len(list), sum(list2)]


count_positives_sum_negatives(arr)


def greeting(op, v1, v2):
    if op == "+":
        return v1+v2
    elif op == "-":
        return v1-v2
    elif op == "*":
        return v1*v2
    elif op == "/":
        return v1/v2


def string_clean(s):
    result = ""
    for i in s:
        if i == "0":
            continue
        elif i == "1":
            continue
        elif i == "2":
            continue
        elif i == "3":
            continue
        elif i == "4":
            continue
        elif i == "5":
            continue
        elif i == "6":
            continue
        elif i == "7":
            continue
        elif i == "8":
            continue
        elif i == "9":
            continue
        result += i
    return result


print(string_clean("This looks5 grea8t!"))