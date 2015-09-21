# generate two prime numbers (7 bits long)
from helper import *


def createKeyPair():
	p = generatePrime()
	q = generatePrime()
	while True:
		if p == q:
			q = generatePrime()
			continue
		else: break

	# create the public key
	n = p*q
	phi = (p-1)*(q-1)

	# find a relative prime of phi and its reverse
	keyPair = extendEuclidean(phi)
	#print keyPair
 	keyPair.append(n)
 	return keyPair



aliceKey = createKeyPair()
trentKey = createKeyPair()


#########################################
# create a certificate for Alice
# consist of pair r, and a signature

r = '00000000'
name = "Alice"
for c in list(name):
	r += intToBinaryString(ord(c), 8)

n = aliceKey[2]
r += intToBinaryString(n, 32)
r += intToBinaryString(aliceKey[1], 32)



hash_r = myHash(r)
print trentKey[0]
s = fastExponentiation(int(hash_r, 2), trentKey[0], trentKey[0]-1)

#########################################
# doing authenticates

nString = intToBinaryString(n, 32)
uString = ""
k,i = 31, 31
while i >= 0:
	if nString[31-i] == "1":
		k = i
		break
	else:
		uString += "0"
		i -= 1

print k

uString = uString + "01"
i -= 2
while i >= 0:
	randBit = getRandomBit()
	uString = uString + str(randBit)
	i -= 1

print nString
print uString


# alice compute h(u) and decrypt it
# hash_u = myHash(uString)
hash_u = "1010101"
v = fastExponentiation(int(hash_u, 2), aliceKey[0], aliceKey[2])
v_encrypted = fastExponentiation(v, aliceKey[1], aliceKey[2])


print "hash_u: " + str(int(hash_u,2))
print "v: " + str(v)
print "aliceKey: " + str(aliceKey[0]) + ", " +  str(aliceKey[1])
print "v_encrypted: " + str(v_encrypted)


print printText


















