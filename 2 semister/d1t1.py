tomSpeed = int(input("Введите скорость  \n"))
jerrySpeed = int(input("Введите скорость Джерри \n"))
distance = int(input("Введите расстояние между ними \n"))
if tomSpeed<=jerrySpeed:
    print("Том не догонит Джерри.")
else:
    print("Том догонит Джерри за ", float(distance/(tomSpeed-jerrySpeed))," секунд")