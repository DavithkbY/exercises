import csv
import collections
file_out = open(r'/Users/greek/PycharmProjects/exercises/old-exams/csv-written-exams/output.txt', 'a')
file_out.truncate(0)

with open('exam-schedule.csv', newline='', encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    lectoren = dict()
    for row in reader:
        if row['Ex. Soortx'] == 'S':
            lectors = row['Lector'].split('/')
            for l in lectors:
                if l not in lectoren:
                    lectoren[l] = 1;
                else:
                    lectoren[l] = lectoren[l] + 1;
    lectoren = collections.OrderedDict(sorted(lectoren.items()))
    for key,value in lectoren.items():
        file_out.write(key + ' ' + str(value) + '\n')
    file_out.close()