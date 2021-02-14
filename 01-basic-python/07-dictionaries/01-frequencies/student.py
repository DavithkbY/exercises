# Write your code here

def frequencies(xs):
    dick = {}
    for x in xs:
        if x not in list(dick):
            dick[x] = 1
        elif x in list(dick):
            dick[x] += 1
    return dick