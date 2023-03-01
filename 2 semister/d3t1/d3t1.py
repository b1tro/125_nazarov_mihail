from bs4 import BeautifulSoup
import requests
import urllib.parse
import random

monthName = str(input('Введите название месяца в котором вы родились\n'))
yearNumber = int(input('Введите год в котором вы родились\n'))

def season_events(number_of_month, year):
    events = []
    url = 'https://ru.wikipedia.org/wiki/Категория:'+ str(number_of_month) + "_" + str(year) + '_года'
    transformedUrl = urllib.parse.quote(url,safe=':/')
    response = requests.get(transformedUrl)
    bs = BeautifulSoup(response.text, "lxml")
    print1 = bs.find('div', class_='mw-category-group').find('a').get('title')
    articles = bs.find_all('div', class_="mw-category-group")
    for article in articles:
        titles = article.find_all('a')
        for title in titles:
            events.append(title.get('title'))
    wiki = open('wiki', 'w+')
    wiki.write("В " + str(year) + " году, в месяце " + str(number_of_month).lower() + " произошли данные события:")
    choosenNumbers = []
    for i in range(0,5):
        currentNumber = random.randint(0,len(events)-1)
        if choosenNumbers.count(currentNumber)==0:
            wiki.write('\n' + events[currentNumber])
            choosenNumbers.append(currentNumber)

season_events(monthName,yearNumber)