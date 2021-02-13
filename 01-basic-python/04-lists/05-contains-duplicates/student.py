# Write your code here

def contains_duplicates(xs):
    list = []
    for i in xs:
        for x in list:
            if i == x:
                return True
        list.append(i)
    return False