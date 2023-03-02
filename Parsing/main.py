import requests
import datetime

print('Привет! Сейчас мы найдем список ближайших фильмов, выпущенных в выбранную дату')
year = str(input('Выбери год выпуска фильма в формате [YYYY]\n'))
month = int(input('Введи месяц в формате [MM]\n'))
day = str(input('Введи день в формате [DD]\n'))

date = str(month) + "." + str(day) + "." + str(year)
if str(month) == ('12'):
    month2 = '01'
else:
    month2 = '0' + str(int(month) + 1)
year2 = str(int(year) + 1)
date2 = str(month2) + "." + str(day) + "." + str(year2)

URL = 'https://api.kinopoisk.dev'
TITLE = '/movie?field=premiere.world&search=' + date + '-' + date2 + '&limit=100'
TOKEN = '&token=R89X55B-GDMM71C-JDCEYKN-HYGAHX7'
takenInformation = requests.get(URL+TITLE+TOKEN)
file = open('Список фильмов', 'w+', encoding="utf-8")
file.write("В дату " + date + "-" + date2 + " были найдены данные фильмы:\n")
print(len(takenInformation.json()['docs']))
for i in range(len(takenInformation.json()['docs'])):
    file.write(takenInformation.json()['docs'][i]['names'][0]['name'])
    file.write('\n')
