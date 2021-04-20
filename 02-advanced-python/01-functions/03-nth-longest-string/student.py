# Write your code here

def nth_longest_string(n, strings):
    sort = sorted(strings, key=len)
    return sort[-n]