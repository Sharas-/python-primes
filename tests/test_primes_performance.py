import timeit
import sys
sys.path = ['..'] + sys.path
import primes
import pytest

if __name__ == '__main__': pytest.main('-s')

def test_list_primes_1_to_1000000():
	_print_statement_time('list(primes.create_prime_iterator(1, 1000000))')

def test_is_prime_1000000000000000():
	_print_statement_time('primes.is_prime_except_2(1000000000000000)')

def _print_statement_time(statement):
	import decimal
	wall_time = timeit.timeit(setup='import primes', stmt=statement, number=1)
	print statement + ' took ' + str(decimal.Decimal(wall_time)) + ' seconds'

#test_is_prime_1000000000000000()
#test_list_primes_1_to_1000000()
