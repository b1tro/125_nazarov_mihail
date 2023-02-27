import random

list1 = []
list2 = []

for i in range(random.randint(49,100)):
    list1.append(random.randint(-1, 9999))
    list2.append(random.randint(-1, 9999))
for x in list1:
    if list2.count(x) == 0:
        print(x)