import csv
import datetime
file_out = open(r'/Users/greek/PycharmProjects/exercises/old-exams/blanket/output.txt', 'a')
file_out.truncate(0)

with open('exam-schedule.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    exams = dict()
    noDuplc = dict()
    for row in reader:
        k = str(row['Lokaal']) +' '+ str(row['Datum'])
        if k not in exams:
            exams[k] = 1
        else:
            exams[k] = exams[k] + 1
    for key,value in exams.items():
        if key in noDuplc:
            print(exams[key])


    print(exams)