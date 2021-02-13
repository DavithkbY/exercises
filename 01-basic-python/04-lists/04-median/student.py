# Write your code here
import math
def median(ns):
    sortedNs= sorted(ns)

    length = len(ns)
    if (length%2) == 0 :
        return (sortedNs[(length//2) - 1] + sortedNs[length//2]) / 2
    else:
        return sortedNs[length//2]