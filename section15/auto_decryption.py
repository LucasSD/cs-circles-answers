# basic decryption program for a Shift cypher/Caesear cypher, must use capital letters
original = input()
list_of_shifts = [] # initialise an empty list of shifted strings
goodness_list = [] # initialise an empty list of goodness ratings for each shift

def goodness_funct(y):
   global goodness_int
   goodness_int += letterGoodness[y - 65] #add goodness rating of each letter. The -65 converts the ascii code to the 'alphabet number'
   return

def shift_cipher(x): 
   shifted_original = '' #initialise an empty string    
   for char in x: # loop to cycle through the input string
      shifted_asci = ord(char) - i # perform the shift of ascii value
      if char == ' ': 
         shifted_original += ' ' # if it's a space, add a space to the shifted_original string
         continue # next character
      elif shifted_asci < 65: # if not a space and if...
         shifted_asci += 26 # correction for cycling 'less than A'
         shifted_original += chr(shifted_asci) #add the shifted character to shifted_original
         goodness_funct(shifted_asci) #add the goodness value of that character to previous total
         continue # next character
      shifted_original += chr(shifted_asci)  # if previous arguments don't apply, add the shifted character to shifted_original
      goodness_funct(shifted_asci) #add the goodness value of that character to previous total
   list_of_shifts.append(shifted_original) # put shifted_original into a list at the index corresponding to the shift
   goodness_list.append(goodness_int) # put goodness_int into list at the index corresponding to the shift
   return 

for i in range(26):# loop for each shift value
   goodness_int = 0 # initiliase an integer to track goodness of each shift
   shift_cipher(original)  
print(list_of_shifts[goodness_list.index(max(goodness_list))]) #print the shifted string which shares the same position as the maximum goodness value