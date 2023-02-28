#file = open('D:\GitHub/125_nazarov_mihail/125_nazarov_mihail/2 semister\d2t1.txt', 'r', encoding="utf-8")
file = "Здесь может быть ваш файл!"
text = (file.read()).split()
print(text)
maxLength = 0
maxLengthWord = ""
maxCountOfWord = 0
maxCountWord = ""
#проверяем текст на выполнения условия
if len(text) < 4:
    print("В тексте меньше 5 слов!")
    exit()

for i in range(len(text)):
# для удобного подсчета слов, убираем все знаки препинания и делаем стандарт в виде нижнего регистра
    text[i] = text[i].lower()
    while (text[i][len(text[i])-1] in "!?.,;\n"):
        text[i] = text[i][:len(text[i])-1]
#проверяем максимум и в случае чего запоминаем слово
    if maxLength < len(text[i]):
        maxLength = len(text[i])
        maxLengthWord = text[i]
    if maxCountOfWord < text.count(text[i]):
        maxCountOfWord = text.count(text[i])
        maxCountWord = text[i]
print("Большая длинна: ", maxLength, ", и это слово: ", maxLengthWord, ". Наиболее повторяющееся слово: ", maxCountWord,
      ", оно повторялось ", maxCountOfWord, "раз.")


