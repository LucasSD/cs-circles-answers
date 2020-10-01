def choose(n, k):
   n_factorial = 1 #initialise
   for i in range (2, n + 1):
      n_factorial *= i # find the product of the natural numbers up to n (n!)
   
   k_factorial = 1 #initialise
   for i in range (2, k + 1):
      k_factorial *= i # find the product of the natural numbers up to k (k!)
      
   sub = n - k 
   sub_factorial = 1 #initialise
   for i in range (2, sub + 1):
      sub_factorial *= i # find (n - k)!
   
   return n_factorial / (k_factorial * sub_factorial) # return the binomial coefficient (n choose r)