def hailstone(n):
   print(int(n))
   
   if n == 1: return # base case to stop the recursion
   elif n % 2 == 0: # if even...
      n /= 2
      hailstone(n) # call function again
   else: #if odd...
      n = 3 * n + 1
      hailstone(n) # call function agan
   return