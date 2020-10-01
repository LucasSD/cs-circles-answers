def naturalNumbers(n):
   list = [] # create an empty list
   for i in range (1, n + 1): # do the block below n times
      list += [i] # concatenate the integer i each time
   return list