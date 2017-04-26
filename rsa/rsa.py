import random, inspect
import rsagen as g
import rsaalg as a
import rsagenpq as pq

#---------------generate p---------------#
p = pq.genp()							# generate p

#---------------generate q---------------#
q = pq.genq()							# generate q

#---------------generate n and phi(n)---------------#
while (q == p):							#regens p and q until they are both prime and not equal
    print("P and Q equal. Generating new p...")
    p = pq.genp()

n = p * q								#calculates n
phin = (p-1) * (q-1)					#calculates phi(n)

#---------------generate e and d---------------#
e = 3									#generate e, set at 3 (to begin)
gcd, d  = a.xgcd(e, phin)				#calls extended euclidian algorithm function and places results in two variables, generating d

while(gcd != 1):						#increases value of e until gcd of e and phi(n) is 1
    e += 1
    gcd, d = a.xgcd(e, phin)
    while (e == phin):					#regens the entire process if all values of e are expended
        print("All values of e expended. Regenerating p and q...")
        p = pq.genp()
        q = pq.genq()
        phin = (p-1) * (q-1)
        e += 1

d = abs(d)  							#ensures d is positive

#---------------results---------------#
print("\n")								#prints final result of p, q, n, phi(n), e, and d
print("Results: ")
print("p = {}".format(p) + "\t\t" + "binary of p = {}".format(g.dectobin(p)))
print("q = {}".format(q) + "\t\t" + "binary of q = {}".format(g.dectobin(q)))
print("n = {}".format(n) + "\t" + "binary of n = {}".format(g.dectobin(n)))
print("phi(n) = {}".format(phin) + "\t" + "binary of phi(n) = {}".format(g.dectobin(phin)))
print("e = {}".format(e) + "\t\t" + "binary of e = {}".format(g.dectobin(e)))
print("d = {}".format(d) + "\t" + "binary of d = {}".format(g.dectobin(d)))
			