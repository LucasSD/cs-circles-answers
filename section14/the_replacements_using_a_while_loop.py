def replace(list, X, Y):
   while list.count(X) > 0: # do it until X is no longer in the list (can also use 'while X in list:')
       list.insert(list.index(X), Y) # insert Y into the desired position
       list.remove(X) # remove the first X
   return list