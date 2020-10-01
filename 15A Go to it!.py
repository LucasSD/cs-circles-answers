def findLine(prog, target):
   for i in range (len(prog)): # scan forwards through each list entry
      if prog[i].startswith(target): #if string at i starts with target substring
         return i #return position i