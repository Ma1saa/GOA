list = []
for i in range(1, 21):
    list.append(i)


list2 = []
for i in range(10, 41):
    if i % 2 == 0:
        list2.append(i)

list3 = []
for i in range(1, 9):
    list3.append(i**2)



list4 = [i for i in range(1, 21)]
list5 = [i for i in range(10, 41) if i % 2 == 0]
list6 = [i**2 for i in range(1, 9)]

list7 = [i*2 for i in range(5, 15) if i % 2 == 0]

