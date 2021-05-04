def naturalNumbers(n):
   list = [1] * n # make a list of the correct length
   for i in range (2, len(list) + 1): #iterate through the list. Position 0 can always remain as '1'
      list[i - 1] = i # ressign list entries
   return list