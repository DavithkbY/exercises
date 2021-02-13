# Write your code here
def coins(one, two, five, goal):
    amount = 0
    for x in range(one):
        amount +=1
        if amount == goal:
            return True
    for y in range(two):
        amount +=2
        if amount == goal:
            return True
    for z in range(five):
        amount +=5
        if amount == goal:
            return True
    return False