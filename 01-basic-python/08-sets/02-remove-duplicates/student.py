# Write your code here

def remove_duplicates(xs):
    notaList = set()
    res = []
    for x in xs:
        if x not in notaList:
            notaList.add(x)
            res.append(x)
    return res