import collections
input = open(r'/Users/greek/PycharmProjects/exercises/old-exams/mario-kart/input.txt', 'r+')
output = open(r'/Users/greek/PycharmProjects/exercises/old-exams/mario-kart/output.txt', 'a')
output.truncate(0)
ranking = 1
points = 100
table = dict()
for player in input:
    if player not in table:
        table[player] = points
        points -= 1
        ranking += 1
    else:
        table[player] = table[player] + points
        points -= 1
        ranking += 1
    if points == 0:
        points = 100
    if ranking == 100:
        ranking = 0
table = sorted(table.items(), key=lambda x: x[1], reverse=True)

top = list(table)[:10]
for key, value in top:
    output.write(key)

input.close()
output.close()