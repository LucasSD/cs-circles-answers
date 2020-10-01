def nestedListContains(NL, target):
   global result
   result = 0
   if target in NL: #if the target integer is in the list
      result += 1  
      return True
   
   for i in NL: #for every entry in the list
      if isinstance(i, list):
         nestedListContains(i, target)
   
   if result > 0: return True
   return False