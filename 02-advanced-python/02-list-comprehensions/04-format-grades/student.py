# Write your code here
def Average(lst):
    return str(round(sum(lst) / len(lst)))


def format_grades(grades):
    s = ''
    for k, v in grades.items():
        avg = Average(v)
        s += k + ': ' + Average(v) + '\n'
    s = s[:-2]
    return s