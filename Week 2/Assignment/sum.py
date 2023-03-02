"""Given an array of integers, find the sum of its elements.
    For example, if the array ar = [1,2,3],
        Calculate 1+2+3 = 6, so return 6."""


def sum(ar):
    total = 0
    for i in ar:
        total += i
    return total

ar = [1, 4, 6, 8]
print(sum(ar))
