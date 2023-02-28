#file = open("D:/GitHub/125_nazarov_mihail/125_nazarov_mihail/2 semister/d2t3.txt",'r',encoding="utf-8")
file = "Здесь может быть ваш файл!"
if (file.read()).replace(" ", ""):
    print("Больше чем 800 символов")
    waitForExit = str(input("Нажмите любую клавишу для выхода"))
    exit()
text = (file.read()).split()
print(len(text))