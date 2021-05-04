def prod(L):
   prod = 1 # initialise variable
   
   for i in range (0, len(L)):
      prod *= L[i] # multiply all entries until end
   
   return prod