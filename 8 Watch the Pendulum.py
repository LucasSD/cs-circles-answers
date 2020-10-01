import math
L = float(input())
A = float(input())

for i in range(10):
   print(float(L * math.cos(A * math.cos(i * math.sqrt(9.8/L))) - L * math.cos(A)))