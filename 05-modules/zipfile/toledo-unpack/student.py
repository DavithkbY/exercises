from zipfile import ZipFile
import sys
import os


def getNumber(name):
    return name.split("_")[1]


def slug(name):
    parts = name.split(' ')
    fname = parts[0]
    lname = parts[1:]
    return '-'.join(s.lower() for s in lname + [fname])


filename = sys.argv[1]
if not os.path.exists('submissions'):
    os.makedirs('submissions')
db = {}
with ZipFile(filename) as zip:
    for file in zip.namelist():
        if file.endswith('.txt'):
            qNumber = getNumber(file)
            txtFile = zip.read(file)
            txtFile = txtFile.decode("utf-8")
            text = txtFile.split()
            text = text[:-1]
            text = text[1:]
            text = slug(' '.join(text))
            path = 'submissions/' + text
            if not os.path.exists(path):
                os.makedirs(path)
            db[qNumber] = path

with ZipFile(filename) as zip:
    for file in zip.namelist():
        if not file.endswith('.txt'):
            qNumber = getNumber(file)
            if (qNumber) in db:
                zip.extract(file, db[qNumber])
