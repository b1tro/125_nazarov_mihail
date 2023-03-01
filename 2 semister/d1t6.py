import random

def whoCanBuy(cost, peopleAndMoney):
    i = 0
    #сортирую по возрастанию
    peopleAndMoneySorted = sorted(peopleAndMoney, key=peopleAndMoney.get)
    #для своего удобства делаю реверс
    peopleAndMoneySorted.reverse()
    #реализую вывод
    print("Скидываться вместе будут:")
    for name in peopleAndMoneySorted:
        if i != 2:
            print(name, "с количеством денег на счету -", peopleAndMoney[name])
            i += 1
        else:
            print("В сделку не входит ", name, "потому имеет всего", peopleAndMoney[name])


COST = random.randint(500,1001)
peopleAndMoney = {'Алиса': random.randint(0,999),'Боб': random.randint(0,999),'Чарли': random.randint(0,999)}
#Делаю значение денег ребятам исходя из условий (x+y+z > цена)
while (peopleAndMoney['Алиса']+peopleAndMoney['Боб']+peopleAndMoney['Чарли'] < COST):
    peopleAndMoney['Алиса'] = random.randint(0, 999)
    peopleAndMoney['Боб'] = random.randint(0, 999)
    peopleAndMoney['Чарли'] = random.randint(0, 999)
print(peopleAndMoney)

whoCanBuy(COST, peopleAndMoney)






