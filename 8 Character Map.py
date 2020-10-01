start = 32
finish = 48
for row_num in range (6):
   chr_string = '' #reset empty
   asc_string = '' # reset empty
   
   for i in range(start, finish):
      chr_string += chr(i) + '   ' # build chr_string
      if row_num == 4 or row_num == 5:
         if i >= 100: asc_string += str(i) + ' ' # build asc_string with smaller spacing
         else: asc_string += str(i) + '  ' # build asc_string    
      else: asc_string += str(i) + '  ' # build asc_string for rows 1 to 3
   
   print('chr:  ' + chr_string)
   print('asc: ' + asc_string)
   start += 16 # increment for new row
   finish += 16 #increment for new row