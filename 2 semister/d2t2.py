def sum_range (start, end):
    if start > end:
        start,end = end,start
    sum = 0
    for i in range(start,end+1):
        sum+=i
    return sum

start = int(input("Введите первое число"))
end = int(input("Введите второе число"))
print("Сумма этих чисел по порядку равна ", sum_range(start,end))