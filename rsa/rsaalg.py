import random, inspect

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
    print("e = {}".format(n1) + "\t" +  "phi(n) = {}".format(n2))
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