def check(card_num):
   # if there are not three spaces in the correct positions or the string is not 19 long
   #or when the spaces are removed, the string is not digits only, print False
   if card_num[4::5] != '   ' or len(card_num) != 19 or \
      card_num.replace(' ', '').isdigit() == False: return False
   else: # if the above are satisfied
      check_sum = 0 # initialise from zero
      for char in card_num.replace(' ', ''): # once spaces are removed, for every character
         check_sum += int(char) # add each digit working through the entire string
      if check_sum % 10 == 0: return True # if total is divisble by 10
      else: return False