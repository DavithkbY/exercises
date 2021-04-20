# Write your code here
import re
def slug(name):
    arr = name.split(' ')
    vnaam = arr[0]
    lnaam = arr[1:]

    return '-'.join(s.lower() for s in lnaam + [vnaam])