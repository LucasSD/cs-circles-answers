def replace(list, X, Y):
   for i in range(list.count(X)): # do it the number of times the entry to be replaced occurs in the list
       list.insert(list.index(X), Y) # insert Y into the desired position
       list.remove(X) # remove the first X
       
   return list