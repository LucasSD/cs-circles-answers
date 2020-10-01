def temp_convert():
   temp = input()
   temp_float = float(temp[:len(temp) - 1]) # cut off the C or F from the end and change to a float
   if temp.endswith('C'): print(str((temp_float * 9 / 5) + 32) + 'F') # convert to F
   else: print(str((temp_float - 32) * 5 / 9) + 'C')  # convert to C 

temp_convert()