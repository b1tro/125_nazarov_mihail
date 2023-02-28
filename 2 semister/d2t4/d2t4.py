import random

playerName = str(input("Введи свое имя!\n"))
number = random.randint(1,101)
attemps = 1
guessNumber = int(input("Угадай мое число!\n"))
while guessNumber != number:
    attemps+=1
    if guessNumber > number:
        guessNumber = int(input("Твое число больше, чем надо!\n"))
    else:
        guessNumber = int(input("Твое число меньше, чем надо!\n"))
print("Поздравляю! Ты победил!")
report = open("Game Results.txt", "w+")
report.write("Игрок: " + str(playerName) + "\nЧисло попыток: " + str(attemps) + "\nЗагаданное число: " + str(number))