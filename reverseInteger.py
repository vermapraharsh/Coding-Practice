#Reverses the order of the input integer, removing leading 0s and ensuring sign is the same
a = -123
b = -567
c = -1200

negFlag = 0
convertString = str(a)
if(convertString[0].isdigit()) != (0 == 0):
    convertString = convertString.replace('-', '')
    negFlag = 1
if(convertString.isdigit()):
    arrayLen = len(convertString)
    tempLen = arrayLen - 1
    tempArray = [None]*arrayLen
    for x in range(0,arrayLen):
        tempArray[tempLen] = convertString[x]
        tempLen = tempLen - 1
    finalStr = "".join(tempArray)
    finalStr = finalStr.lstrip('0')
    if (negFlag == 1):
        finalStr = "-" + finalStr
    print(finalStr)
