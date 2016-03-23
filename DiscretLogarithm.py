import gmpy

entierLimite = 1000000

def ModPowIte(a, exp, n):
	ret = a
	for i in range(exp-1):
		ret = ret*a
		ret = ret%n
	return ret

def isprime(n):
	prob = gmpy.is_prime(n)
	if(prob == 2 or prob == 1):
		return True
	else:
		return False

def fact(n):
	res = list()
	tmp = n
	for i in range(2, entierLimite):
		if( isprime(i) and (tmp%i == 0) ):
			res.append(i)
			tmp = tmp / i
	return res

print ModPowIte(5, 3, 13)

print fact(4)
