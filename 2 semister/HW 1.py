import math
import json
import urllib.request

api = "https://api.wheretheiss.at/v1/satellites/25544"
check = urllib.request.urlopen(api)
data = json.loads(check.read())
print(data)
planets = {'Меркурий': [3.302 * math.pow(10,23), 92 * math.pow(10,9)],
           'Венера': [4.8685 * math.pow(10,24), 42 * math.pow(10,9)],
           'Марс': [6.419 * math.pow(10,23), 79 * math.pow(10,9)],
           'Юпитер': [1.8986 * math.pow(10,27), 628 * math.pow(10,9)],
           'Сатурн': [5.6846 * math.pow(10,26), 1278 * math.pow(10,9)],
           'Уран': [8.6832 * math.pow(10,25), 2721 * math.pow(10,9)],
           'Нептун': [1.0243 * math.pow(10, 26), 4348 * math.pow(10,9)],
           'Плутон': [1.31 * math.pow(10, 22), 6239 * math.pow(10,9)],
           'Луна': [7.35 * math.pow(10, 22), 384399 * math.pow(10,3)],
           'МКС': [42 * math.pow(10,4), data['altitude'] * math.pow(10,3)]}
theEarthMass = 5.976 * math.pow(10,24)
G = 6.6743 * math.pow(10,-11)
def findOutGravitaion(G, m1, m2, R):
    return (G*m1*m2)/(math.pow(R,2))

nameOfAPlanet = input('Напишите название объекта ')
print(findOutGravitaion(G,theEarthMass,planets[nameOfAPlanet][0], planets[nameOfAPlanet][1]))
