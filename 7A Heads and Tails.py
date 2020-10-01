inputString = input()
newFirst = inputString[len(inputString)-1]
newLast = inputString[0]
middleString = (inputString[1:len(inputString)-1])
outputString = newFirst + middleString + newLast
print(outputString)