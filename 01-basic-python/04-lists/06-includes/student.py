# Write your code here

def includes(xs,ys):

    if len(xs)==0 or len(ys) == 0:
        return True
    for x in xs:
        if x in ys:
            return True
    return False