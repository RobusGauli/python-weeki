from itertools import islice

class TypeContract:
	_ty = None
	@classmethod
	def check(cls, value):
		if not isinstance(value, cls._ty):
			raise TypeError(f'Expected the value of type {cls._ty}')


class Integer(TypeContract):
	_ty = int

class Float(TypeContract):
	_ty = float

class String(TypeContract):
	_ty = str



def golden_numbers(a, b):
  Integer.check(a)
  Integer.check(b)
  yield a
  yield from golden_numbers(b, a + b)


if __name__ == '__main__':

	first_fifty_fib_numbers = list(islice(golden_numbers(0, 1), 50))
	first_fifty_lucas_numbers = list(islice(golden_numbers(2, 1), 50))
	print(first_fifty_fib_numbers, first_fifty_lucas_numbers)


