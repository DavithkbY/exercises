old_lines = set(
    (line.strip().lower() for line in open(r'/Users/greek/PycharmProjects/exercises/old-exams/absentees/attending.txt', 'r+')))
file_new = open(r'/Users/greek/PycharmProjects/exercises/old-exams/absentees/all.txt', 'r+')
file_diff = open(r'/Users/greek/PycharmProjects/exercises/old-exams/absentees/absentees.txt', 'a')
file_diff.truncate(0)
for line in file_new:
    if line.strip().lower() not in old_lines:
        file_diff.write(line.lower())
file_new.close()
file_diff.close()
