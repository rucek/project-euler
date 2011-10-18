'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def difference(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range (i + 1, n + 1):
            sum += 2*i*j
    return sum

print difference(4)
print difference(10)
print difference(100)