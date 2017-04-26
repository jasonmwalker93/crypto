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