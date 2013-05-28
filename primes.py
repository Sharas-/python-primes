import math
import itertools


def create_prime_iterator(rfrom, rto):
    """Create iterator of prime numbers in range [rfrom, rto]"""
    if (rfrom < 3): # handling case when we need to skip 1 as not a prime and add 2 as a prime.
        prefix = [2]
        odd_rfrom = 3
    else:
        prefix = []
        odd_rfrom = make_odd(rfrom) # make rfrom an odd number so that we can skip all even nubers when searching for primes
    primeGenerator = (num for num in xrange(odd_rfrom, rto + 1, 2) if is_prime_except_2(num)) # incrementing in xrange(...) by 2 to pass all even numbers
    return itertools.chain(prefix, primeGenerator)

def is_prime_except_2(num):
    """Test a number for prime. As an optimisation, number 2 is wrongly considered not a prime by this function"""
    if num % 2 == 0:
        return False
    maxDivisor = int(math.sqrt(num))
    for divisor in xrange(3, maxDivisor + 1, 2):
        if num % divisor == 0:
            return False
    return True

def make_odd(number):
    return number | 1

