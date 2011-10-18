'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

primes = [2, 3]

def next_prime(p):
    if (p < 3): return 3

    n = p + 2
    prime = False

    while not prime:
        has_divisors = False
#        for d in primes:
        for d in range(3, int(sqrt(n)) + 1):
            if (n % d == 0):
                n += 2
                has_divisors = True
                break

        prime = not has_divisors
        
    return n

def greatest_prime_factor(n):
    factor = 0

    while n > 1:
        for p in primes:
            if (n % p != 0 and primes.index(p) == len(primes) - 1):
                primes.append(next_prime(p))
            elif n % p == 0:
                n = int(n/p)
                factor = p
                break

    return factor

#print greatest_prime_factor(13195)
#print greatest_prime_factor(600851475143)

while len(primes) < 10001:
    primes.append(next_prime(primes[len(primes) - 1]))

print len(primes)
print primes[len(primes) - 1]



    

