def postalValidate(S):
   no_spaces = S.replace(' ', '') # remove any spaces
   
   if no_spaces[0:5:2].isalpha() == True and no_spaces[1:6:2].isdigit() == True \
      and len(no_spaces) == 6: # if no_spaces is in format L#L#L# where Ls are letters and #s are digits and no_spaces is 6 long
      return no_spaces.upper() # no_spaces with uppercase letters
   else: return False # False as it's not in correct format