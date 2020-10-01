S = input() # e.g. 45+38

for i in range(1, int(len(S))):
   if S[i] == '+': plus_position = i
   
num1 = int(S[0:plus_position])
num2 = int(S[plus_position + 1:int(len(S))])

print(num1 + num2)