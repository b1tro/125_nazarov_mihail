import random
def magic(sumOfSequence,X):
    return( sumOfSequence%X==0)
    for i in range(len(sequenceOfNumbers)-1):
        sequenceOfNumbers[0]+=i
        sequenceOfNumbers.pop()
        #Зачем создавать новый массив, если можно складывать первое число с последним, а далее удалять его

X = random.randint(0,9999 * 100)  # чтобы не брать огромные числа, возьму от 1 до максимально возможной суммы последовательности
sequenceOfNumbers = [random.randint(-1,9999) for i in range(random.randint(4,100))]


print(magic(sequenceOfNumbers[0],X), "\nЗначение Х: ", X, "\nЗначение суммы последовательности: ", sequenceOfNumbers[0])

