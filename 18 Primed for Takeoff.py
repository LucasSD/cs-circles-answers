isPrime = [False, False] + [True] * 999999 # choose how long you want the T/F table to be, everything True at start except 0 and 1

def change_multiples(x):
   for x in range(x + x,len(isPrime), x): # for all the muliples of prime but not prime itself
      if isPrime[x] == True:
         isPrime[x] = False #replace True with False

def isItPrime(N): 
  for D in range(2, N): # for all factors of N, up to the square root of N...
    if (D * D > N): break          
    if N % D == 0:
       isPrime[N] = False #replace True with False
  change_multiples(N)
      
for i in range(2, len(isPrime)):
   if isPrime[i] == True:
      isItPrime(i)