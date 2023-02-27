import random

S = []
D = []
#создаем N
for i in range(random.randint(50,101)):
    S.append(random.randint(1,30))
    D.append(random.randint(1, 30))
    if S[i] == D[i]:
        print("Момент! Его номер:", i, "Спрос:", S[i], "Предложение:", D[i])