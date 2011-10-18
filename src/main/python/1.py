'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

number of numbers divisible by d less or equal n: int(n/d)
sum of n first terms in an arithmetic sequence: Sn = n*(a1+an)/2
    if first term equals the difference d: Sn = d*n*(n+1)/2
'''

from datetime import datetime

def first(limit):
    start = datetime.now()
    sum = 0
    for i in range(1, limit):
        if (i % 3 == 0 or i % 5 == 0):
            #print i
            sum += i

    print sum
    print (datetime.now() - start)

def better(limit):
    start = datetime.now()
    sum = 0

    i = 3
    j = 5
    while (i < limit):
        sum += i
        i += 3

    while (j < limit):
        sum += j
        j += 5

    k = 15
    while (k < limit):
        sum -= k
        k += 15

    print sum
    print (datetime.now() - start)

def best(limit):
    start = datetime.now()

    number = limit - 1
    print sum_of_divisors_mod(number, 3) + sum_of_divisors_mod(number, 5) - sum_of_divisors_mod(number, 15)

    print (datetime.now() - start)

def sum_of_divisors_mod(number, modulus):
    n = int(number / modulus)
    return modulus * n * (n+1) / 2

limit = 10000
first(limit)
better(limit)
best(limit)