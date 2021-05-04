S = input() #e.g. 47+91
position = 1

while S[position] != '+':
    position +=1   
plus_position = position

num1 = int(S[0:plus_position])
num2 = int(S[plus_position + 1:int(len(S))])

print(num1 + num2)