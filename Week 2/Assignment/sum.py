"""Given an array of integers, find the sum of its elements.
    For example, if the array ar = [1,2,3],
        Calculate 1+2+3 = 6, so return 6."""

ar = [1, 5, 5, 8, 5, 7, 8, 9]
sum = 0
for i in ar:
    sum += i

print(sum)
