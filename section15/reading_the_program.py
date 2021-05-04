def getBASIC():
   line = input()
   list = [] # create an empty list
   while line.count('END') <= 1: # execute the while block until you reach the final line of BASIC code which contains 'END'
      
      list.append(line) # append the list of input srings
      if line.endswith('END'): #exit the while loop when you reach the final line with 'END'
         break
      line = input() # read the next line of input
      
   return list