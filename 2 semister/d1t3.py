import random

list1 = []
list2 = []

for i in range(random.randint(49,100)):
    list1.append(random.randint(-1, 9999))
    list2.append(random.randint(-1, 9999))
for x in list1:
    if list2.count(x) == 0:
        for k in range(list2.count(x)):
            list2.remove(x)
#Второй лист в итоге изменяется, но в условиях задачи сказано вывести это отдельным листом, поэтому использовал второй, чтобы не тратить лишнюю память
print(list2)

