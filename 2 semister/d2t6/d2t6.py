import csv
import datetime
import time

file = open("rows_300", mode="w+", encoding='utf-8')
fileWriter = csv.writer(file, delimiter=' ')
fileWriter.writerow(["Номер","Дата","Время","Секунда","Микросекунда"])
for i in range(1, 301):
    currentTime = datetime.datetime.now()
    fileWriter.writerow([i, datetime.date.today(), currentTime.strftime("%H:%M"), currentTime.second, currentTime.microsecond])
    time.sleep(0.01)