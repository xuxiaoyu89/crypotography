from random import *
from math import *

def getRandomBit():
	r = randint(0,2**20)
	result = 1 if r%2 == 1 else 0
	print "random number: ", r, ", last bit: ", result
	return result

def multModM(x, y, m):
	return (x*y)%m

def raiseModM():
	return

def isPrime(n):
	# use Miller Rabin Algorithm to check if n is a prime
	a = randint(1,n+1)
	y = 1
	k = int(log(n,2))
	remain = n-1
	for i in xrange(k, -1, -1):
		xi = remain/(2**i)
		#print remain, xi
		remain = remain%(2**i)
		z = y
		y = multModM(y,y,n)
		if y==1 and z!= 1 and z!=(n-1):
			return False
		if xi == 1:
			y = multModM(y, a, n)
		#print i, xi, z, y

	if y != 1:
		return False
	return True

def inverse(e):
	# find the multiplicatve inverse of e
	return

def generateCandidate():
	n = 65
	for i in xrange(1,6):
		rBit = getRandomBit()
		n += rBit*(2**i)
	print "genereated: ", n
	return n

def generatePrime():
	while True:
		n = generateCandidate()
		# test if n is prime
		flag = True
		for i in xrange(21):
			temp = isPrime(n)
			flag = flag and temp
		if flag: return n
		else: continue
q = generatePrime();


def extendEuclidean(phi): 
	phi, e = phi, 3
	d = 0
	while True:
		r1, r2 = phi, e
		q = r1/r2
		q_1 = q
		q_2 = q
		r3 = r1%r2
		s1, t1 = 1, 0
		s2, t2 = 0, 1
		s, t = 1, 0
		i = 1
		while r3!=0:
			r1, r2 = r2, r3
			q = r1/r2
			r3 = r1%r2
			if i == 1:
				s1, t1 = s,t
				s, t = 0, 1
				q_1 = q
			else:
				s2, t2 = s1, t1
				s1, t1 = s, t   
				s = s2 - q_2*s1
				t = t2 - q_2*t1
				q_2 = q_1
				q_1 = q

			print q, r1, r2, r3, s, t 
			i += 1

		if r2 == 1:
			# e is relative prime of phi
			# find the inverse
			d = t1 - q_2*t
			if d < 0: d += phi
			return [d, e]
		else:
			# continue looking 
			e += 1
			continue


def intToBinaryString(n, length):
	digits = []
	r = n
	while r > 0:
		rightBit = str(r%2)
		digits.append(rightBit)
		r = (r-r%2)/2
	while len(digits) < length:
		digits.append('0')

	digits.reverse()
	return "".join(digits)


def fastExponentiation(a, x, n):
	y = 1
	k = int(log(x,2))
	remain = x;
	for i in xrange(k, -1, -1):
		y = multModM(y, y, n)
		xi = remain/(2**i)
		remain = remain%(2**i)
		if xi == 1:
			y = multModM(a, y, n)
	return y

def stringXOR(s1, s2):
	result = []
	for i in xrange(len(s1)):
		result.append(str(int(s1[i]) ^ int(s2[i])))
	return "".join(result)


def myHash(s):
	result = s[0:8]
	i = 8
	while i < len(s):
		result = stringXOR(result, s[i:i+8])
		i += 8
	return result




