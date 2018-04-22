from itertools import islice
from functools import wraps
from inspect import signature

class Contract:
	_ty = None

	@classmethod
	def check(cls, val):
		if not isinstance(val, cls._ty):
			raise TypeError(f'Expected the value of type {cls._ty}')

class Integer(Contract):
	_ty = int

class Float(Contract):
	_ty = float

class String(Contract):
	_ty = str




def enforce_type(func):
	annotation = func.__annotations__
	sig = signature(func)
	@wraps(func)
	def wrapper(*args, **kwargs):
		bound = sig.bind(*args, **kwargs)
		for key, val in bound.arguments.items():
			if key in annotation:
				annotation[key].check(val)
		return func(*args, **kwargs)
	return wrapper

@enforce_type
def golden_numbers(a: Integer, b: Integer):
	yield a
	yield from golden_numbers(b, a + b)

@enforce_type
def need_string(arg: String):
	print(f'{arg} must be of type String')

@enforce_type
def sum_two(a: Float, b: Float):
	return a + b

if __name__ == '__main__':
	need_string('sad')
	sum_two(3, 3)
	

