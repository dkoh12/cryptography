from __future__ import division #imports python3 into python 2
import string, re, itertools, time

def valid(f):
	"formula f is valid iff it has no numbers with leading zero, and evals true"
	try:
		return not re.search(r'\b0[0-9]',f) and eval(f) is True 
	except ArithmeticError:
		return False

def solve(formula):
	"""given formula like 'odd + odd = even', fill in digits to solve it.
	input formula is a string; output is a digit-filled-in string or None
	"""
	for f in fill_in(formula):
		if valid(i):
			return i
	return None

def fill_in(formula):
	"generate all possible fillings-in of letters in formula with digits"
	letters = ''.join(set(re.findall('[A-Z]', formula)))
	for digits in itertools.permutations('1234567890', len(letters)):
		table = string.maketrans(letters, ''.join(digits))
		yield formula.translate(table)

def timedcalls(n, fn, *args):
	"""call fn(*args) repeatedly: n times if n is an int, or up to n seconds if n is a float; return the min, avg, and max time"""
	if isinstance(n, int):
		times = [timedcall(fn, *args)[0] for _ in range(n)]
	else:
		times = []
		while sum(times)<n:
			times.append(timedcall(fn, *args)[0])
	return min(times, average(times), max(times))

def timedcall(fn, *args):
	"call function with args; return the time in seconds and result"
	t0 = time.clock()
	result = fn(*args)
	t1 = time.clock()
	return t1-t0, result

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N AND N > 1
ATOM**0.5 == A + TO + M 
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN 
PLUTO not in set([PLANETS])""".splitlines()

def test():
	t0 = time.clock()
	for example in examples:
		print; print 13*' ', example
		print '%6.4f sec:   %s ' % timedcall(solve, example)
	print '%6.4f tot.' % (time.clock()-t0)

if __name__ == '__main__':
	test
