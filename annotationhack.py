from itertools import islice

def golden_numbers(a, b):
	yield a 
	yield from golden_numbers(b, a + b)




if __name__ == '__main__':

	first_fifty_fib_numbers = list(islice(golden_numbers(0, 1), 50))
	first_fifty_lucas_numbers = list(islice(golden_numbers(2, 1), 50))
	print(first_fifty_fib_numbers, first_fifty_lucas_numbers)


