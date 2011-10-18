'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Find the sum of all the even-valued terms in the sequence which do not exceed four million.

the ratio between two consecutive terms: Phi = F(n)/F(n-1)
as every third term of the sequence is even, the ratio between even terms is: Phi^3
'''

def sum_of_even_terms(limit):
    i = 1
    j = 2
    k = 0
    sum = 2

    while k <= limit:
        k = i + j
        if k % 2 == 0:
            sum += k

        i, j = j, k

    return sum

print "sum: " + str(sum_of_even_terms(4000000))