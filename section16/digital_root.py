def digitalRoot(n):
   if n < 10: return n # base case
   return digitalRoot(digitalSum(n)