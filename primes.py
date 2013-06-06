import math
import itertools


def create_prime_iterator(rfrom, rto):
    """Create iterator of prime numbers in range [rfrom, rto]"""
    prefix = [2] if rfrom < 3 and rto > 1 else [] # include 2 if it is in range separately as it is a "weird" case of even prime
    odd_rfrom = 3 if rfrom < 3 else make_odd(rfrom) # make rfrom an odd number so that we can skip all even nubers when searching for primes, also skip 1 as a non prime odd number.
    odd_numbers = (num for num in xrange(odd_rfrom, rto + 1, 2))
    prime_generator = (num for num in odd_numbers if not has_odd_divisor(num))
    return itertools.chain(prefix, prime_generator)

def has_odd_divisor(num):
    """Test whether number is evenly divisable by odd divisor."""
    maxDivisor = int(math.sqrt(num))
    for divisor in xrange(3, maxDivisor + 1, 2):
        if num % divisor == 0:
            return True
    return False

def make_odd(number):
    """Make number odd by adding one to it if it was even, otherwise return it unchanged"""
    return number | 1

