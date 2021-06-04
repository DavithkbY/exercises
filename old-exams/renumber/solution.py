import re
file_in = open(r'/Users/greek/PycharmProjects/exercises/old-exams/renumber/input.txt', 'r+')
file_out = open(r'/Users/greek/PycharmProjects/exercises/old-exams/renumber/output.txt', 'a')
file_out.truncate(0)
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
count = 1
for line in file_in:
    originalline = line
    gewijzigd = False
    if len(line) == 10:
        if 'Chapter' in line:
            if RepresentsInt(line[-2]):
                file_out.write('Chapter ' + str(count) + '\n')
                count += 1
                gewijzigd = True
    if gewijzigd == False:
        file_out.write(originalline)
file_in.close()
file_out.close()
