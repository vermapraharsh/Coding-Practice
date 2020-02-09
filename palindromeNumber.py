#Tests if a number is a palindrome or not
a = -121
b = 121
c = -1200
d = 120021

convertString = str(b)
if(convertString[0].isdigit()) != (0 == 0):
    print("False")
if(convertString.isdigit()):
    arrayLen = len(convertString)
    tempLen = arrayLen - 1
    tempArray = [None]*arrayLen
    for x in range(0,arrayLen):
        tempArray[tempLen] = convertString[x]
        tempLen = tempLen - 1
    finalStr = "".join(tempArray)
    if(finalStr == convertString):
        print("True")
