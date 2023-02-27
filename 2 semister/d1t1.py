tomSpeed = int(input("Введите скорость Тома"))
jerrySpeed = int(input("Введите скорость Джерри"))
distance = int(input("Введите расстояние между ними"))
if tomSpeed<=jerrySpeed:
    print("Том не догонит Джерри.")
else:
    print("Том догонит Джерри за ", float(distance/(tomSpeed-jerrySpeed))," секунд")