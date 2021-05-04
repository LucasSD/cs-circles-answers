letter = input()
if ord(letter) >= ord('A') and ord(letter) <= ord('Z'): # if it's a capital letter
   print(ord(letter) - 64) # convert to alphavet number 1-26
else:
   print('invalid')