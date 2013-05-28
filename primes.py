import math
import itertools


def create_prime_iterator(rfrom, rto):
    """Create iterator of prime numbers in a range [rfrom, rto]"""
    if(rfrom < 3):
        rfrom = 3
        prefix = [2]
    else:
        prefix = []
    primeGenerator = (num for num in xrange(rfrom, rto + 1) if is_prime_except_2(num))
    return itertools.chain(prefix, primeGenerator)

def is_prime_except_2(num):
    """Test a number for prime except number 2"""
    if num % 2 == 0:
        return False
    maxDivisor = int(math.sqrt(num))
    for divisor in xrange(3, maxDivisor + 1, 2):
        if num % divisor == 0:
            return False
    return True


