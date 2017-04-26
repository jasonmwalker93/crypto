import random, inspect
import rsagen as g
import rsaalg as a

def genp():
    print("Generating p...")
    p = g.genrand()							#generates random p
    print("p = {}".format(p) + "\n")

    flag = True								#performs 20 primality tests on generated p
    for _ in range(20):
        if (a.primetest(p) == False):
            flag = False

    if (flag == True):						#if flag has not been changed to False, p passed all primality tests
        print("Number is perhaps prime." + "\n")
    else:
        while (flag == False):				#otherwise it failed, and a new p is generated (and test) until it changes the flag to True
            print("Number is not prime. Generating a new p..." + "\n")
            p = g.genrand()
            print("p = {}".format(p) + "\n")

            flag = True
            for _ in range(20):
                if (a.primetest(p) == False):
                    flag = False
        print("Number is perhaps prime." + "\n")
    return p

def genq():
    print("Generating q...")
    q = g.genrand()							#generates random p
    print("q = {}".format(q) + "\n")

    flag = True								#performs 20 primality tests on generated p
    for _ in range(20):
        if (a.primetest(q) == False):
            flag = False

    if (flag == True):						#if flag has not been changed to False, p passed all primality tests
        print("Number is perhaps prime." + "\n")
    else:
        while (flag == False):				#otherwise it failed, and a new p is generated (and test) until it changes the flag to True
            print("Number is not prime. Generating a new q..." + "\n")
            q = g.genrand()
            print("p = {}".format(q) + "\n")

            flag = True
            for _ in range(20):
                if (a.primetest(q) == False):
                    flag = False
        print("Number is perhaps prime." + "\n")
    return q