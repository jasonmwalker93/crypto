import random, inspect

def dectobin(n1):						#converts a decimal number to a binary number
    randbin = int(n1)
    binStr = ""
    while randbin > 0:
        binStr = str(randbin % 2) + binStr
        randbin = randbin // 2
    while(len(binStr) < 32):
        binStr = "0" + binStr
    return binStr

def genint():							#randomly generates a number between 1 and 2,147,483,647 (decimal equivalant of max 32 bit number)
        randint = random.randint(1,2147483647)
        print("\tRandomly generated number: {}".format(randint))
        return int(randint)

def genbit(n1):							#converts a number to binary and returns the lsb
    binStr = dectobin(n1)
    print("\tBinary of randomly generated number: {}".format(binStr))	#prints binary of randomly generated number ot screen
	
    binList = list(binStr)				#converts randomly generated number to list and removes all elemtents by the last
    while len(binList) != 1:
        binList.remove(binList[0])
	
    lsb = int(binList[0])				#converts rightmost character (bit) of rgn to int
    print("\tLeast significant bit of randomly generated number: {}".format(lsb))
    return lsb							#returns lsb in int format
	
def genrand():							#generates 7 bit random number
    srnum = []
    for _ in range(25):
        srnum.append(0)
    srnum.append(1)						#begins array with leading bit
    srnum.append(genbit(genint()))		#randomly generates a bit by calling genint to gen
    srnum.append(genbit(genint()))		#a random number, then genbit to convert it to its lsb
    srnum.append(genbit(genint()))		#then appends that bit to the existing array
    srnum.append(genbit(genint()))
    srnum.append(genbit(genint()))
    srnum.append(1)						#concludes array with ending bit 1
    srnum = ''.join(map(str, srnum))	#converts array to integer
	
    print("\tGenerated bit string: {}".format(srnum))
    return int(srnum, 2)
	
def primetest(n1):					   	#tests primality of a number
    a = random.randint(1,n1)		   	#generates 32 bit random a such that 0 < a < n
    y = 1
	
    print("Performing primality test...")
    print("n = {}".format(n1) + "\t" + "a = {}".format(a))
	
    b = str(bin(n1-1))
    binstr = []
    for digit in b:
        binstr.append(digit)
    del binstr[0:2]
	
    k = len(binstr)
	
    for i in range(k):				 	#performs modified Rabin-Miller algorithm
        z = y
        y = y*y%n1
        if (y == 1 and z !=1 and z != n1-1):
            print("Failed!")
            print("--------------------------")
            return False
        if (binstr[i] == '1'):
            y = y*a%n1
        print("i = {}".format(i) + "\t" +  "z = {}".format(z) + "\t" + "y = {}".format(y))
    if (y != 1):
        print("Failed!")
        print("--------------------------")
        return False
    else:
        print("Passed!")
        print("--------------------------")
        return True
		
def xgcd(n1, n2):						#performs extended euclidian algorithm
    print("Performing extended euclidian algorithm...")
    print("e = {}".format(e) + "\t" +  "phi(n) = {}".format(phin))
    a1 = 1
    a0 = 0
    b0 = 0
    b1 = 1
    while n2 != 0:
        x, n1, n2 = n1 // n2, n2, n1 % n2
        a1, a0 = a0, a1 - x * a0
        b0, b1 = b1, b0 - x * b1
        print("x = {}".format(x) + "\t" +  "a0 = {}".format(a0) + "\t" + "a1 = {}".format(a1) + "\t" + "b0 = {}".format(b0) + "\t" + "b1 = {}".format(b1) + "\t" + "n1 = {}".format(n1))
    print("Returning gcd = {}".format(n1) + " and d = {}".format(a1))
    if (n1 == 1):
        print("Passed!")
    else:
        print("Failed!")
    print("--------------------------")
    return n1, a1

#---------------generate p---------------#
print("Generating p...")
p = genrand()							#generates random p
print("p = {}".format(p) + "\n")

flag = True								#performs 20 primality tests on generated p
for _ in range(20):
    if (primetest(p) == False):
        flag = False

if (flag == True):						#if flag has not been changed to False, p passed all primality tests
    print("Number is perhaps prime." + "\n")
else:
    while (flag == False):				#otherwise it failed, and a new p is generated (and test) until it changes the flag to True
        print("Number is not prime. Generating a new p..." + "\n")
        p = genrand()
        print("p = {}".format(p) + "\n")

        flag = True
        for _ in range(20):
            if (primetest(p) == False):
                flag = False
    print("Number is perhaps prime." + "\n")

#---------------generate q---------------#
print("Generating q...")
q = genrand()							#generates random q
print("q = {}".format(q) + "\n")

flag = True
for _ in range(20):						#performs 20 primality tests on generated q
    if (primetest(q) == False):
        flag = False

if (flag == True):						#if flag has not been changed to False, q passed all primality tests
    print("Number is perhaps prime." + "\n")
else:									#otherwise it failed, and a new q is generated (and test) until it changes the flag to True
    while (flag == False):
        print("Number is not prime. Generating a new q..." + "\n")
        q = genrand()
        print("q = {}".format(q)+ "\n")

        flag = True
        for _ in range(20):
            if (primetest(q) == False):
                flag = False
    print("Number is perhaps prime." + "\n")

#---------------generate n and phi(n)---------------#
while (q == p):							#regens p and q until they are both prime and not equal
    print("P and Q equal. Generating new p...")
    p = genrand()
    print("p = {}".format(p) + "\n")

    flag = True
    for _ in range(20):
        if (primetest(p) == False):
            flag = False

n = p * q								#calculates n
phin = (p-1) * (q-1)					#calculates phi(n)

#---------------generate e and d---------------#
e = 3									#generate e, set at 3 (to begin)
gcd, d  = xgcd(e, phin)					#calls extended euclidian algorithm function and places results in two variables, generating d

while(gcd != 1):						#increases value of e until gcd of e and phi(n) is 1
    e += 1
    gcd, d = xgcd(e, phin)
    while (e == phin):					#regens the entire process if all values of e are expended
        print("All values of e expended. Regenerating p and q...")
        p = genrand()
        print("p = {}".format(p) + "\n")

        flag = True
        for _ in range(20):
            if (primetest(p) == False):
                flag = False

        if (flag == True):
            print("Number is perhaps prime.")
        else:
            while (flag == False):
                print("Number is not prime. Generating a new p...")
                p = genrand()
                print("p = {}".format(p) + "\n")

                flag = True
                for _ in range(20):
                    if (primetest(p) == False):
                        flag = False
            print("Number is perhaps prime.")

            q = genrand()
            print("q = {}".format(q)+ "\n")

            flag = True
            for _ in range(20):
                if (primetest(q) == False):
                    flag = False

            if (flag == True):
                print("Number is perhaps prime.")
            else:
                while (flag == False):
                    print("Number is not prime. Generating a new q...")
                    q = genrand()
                    print("q = {}".format(q) + "\n")

                    flag = True
                    for _ in range(20):
                        if (primetest(q) == False):
                            flag = False
                print("Number is perhaps prime.")

            phin = (p-1) * (q-1)
            e += 1

if (d < 0):								#ensures d is positive
	d = abs(d)

#---------------results---------------#
print("\n")								#prints final result of p, q, n, phi(n), e, and d
print("Results: ")
print("p = {}".format(p) + "\t\t" + "binary of p = {}".format(dectobin(p)))
print("q = {}".format(q) + "\t\t" + "binary of q = {}".format(dectobin(q)))
print("n = {}".format(n) + "\t" + "binary of n = {}".format(dectobin(n)))
print("phi(n) = {}".format(phin) + "\t" + "binary of phi(n) = {}".format(dectobin(phin)))
print("e = {}".format(e) + "\t\t" + "binary of e = {}".format(dectobin(e)))
print("d = {}".format(d) + "\t" + "binary of d = {}".format(dectobin(d)))

			