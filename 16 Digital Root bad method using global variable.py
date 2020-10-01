def digitalRoot(n):
   global x
   x = digitalSum(n) # initialise a global variable of the digital sum of n
   if x < 10: return x # if the digital sum becomes the digital root (single digit)...
   else:
      digitalRoot(x) # call the function again on a new n argument
   return x