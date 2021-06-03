import json
from datetime import datetime
from collections import OrderedDict
# Opening JSON file
file_out = open(r'/Users/greek/PycharmProjects/exercises/old-exams/blanket/output.txt', 'a')
file_out.truncate(0)
with open('input.txt') as json_file:
    data = json.load(json_file)
    ordered_data = OrderedDict(
    sorted(data.items(), key = lambda x:datetime.strptime(x[0], '%d/%m/%Y'), reverse=False))
    for key, value in ordered_data.items():
        mean = int(round(sum(value)/len(value)))
        file_out.write(str(mean)+'\n')