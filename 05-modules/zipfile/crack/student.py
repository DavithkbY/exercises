from zipfile import ZipFile
import sys
import os
import string, random




cracked = False
while cracked == False:
    try:
        with ZipFile('crack.zip') as zip:
            rand = str.encode(''.join(random.choices(string.ascii_letters.lower(), k=4)))
            result = zip.read('file.txt', pwd=rand)
            print(result.decode('utf-8'))
            print(rand)
            cracked = True
    except:
        continue
    break