import requests
import datetime

URL = 'https://api.kinopoisk.dev'
limit = 100
TITLE_LIMIT = '/v1/movie?field=premiere.world&limit=' + str(limit)
TOKEN = '&token=R89X55B-GDMM71C-JDCEYKN-HYGAHX7'
day = int(input("Введите день\n"))
month = int(input("Введите месяц\n"))
year = int(input("Введите год\n"))
date = datetime.datetime(year,month,day)
dateOneMoreDay = date
dateOneMoreDay += datetime.timedelta(days=1)
date = date.strftime("%d.%m.%Y")
dateOneMoreDay = dateOneMoreDay.strftime("%d.%m.%Y")
search_url= "&search=" + str(date) + "-" + str(dateOneMoreDay)
filmesAndRating = {}
accessUrl = URL + TITLE_LIMIT + TOKEN + search_url
access = requests.get(accessUrl)
for i in range(len(access.json()['docs'])):
   filmesAndRating[access.json()['docs'][i]['names'][0]['name']] = access.json()['docs'][i]['rating']['kp']
sorted_keys = sorted(filmesAndRating, key=filmesAndRating.get, reverse=True)
sortedFilmsByRating = {}
for w in sorted_keys:
    sortedFilmsByRating[w] = filmesAndRating[w]
file = open("Список фильмов", 'w+', encoding="utf-8")
file.write('Привет! Вот список фильмов на дату ' + str(date) +"\n")
counter = 0
for key, value in sortedFilmsByRating.items():
    counter+=1
    file.write(str(counter) + ". " + str(key) + ". Его рейтинг на КиноПоиске: " + str(value) +"\n")






