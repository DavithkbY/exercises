# Write your code here
from operator import itemgetter
def longest_string(strings):
    return max(strings, key=lambda s: len(s))