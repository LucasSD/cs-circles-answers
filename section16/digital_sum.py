def digitalSum(n):
   if n < 10: # if n is a single digit
      global dig_sum_counter
      dig_sum_counter = n # records the first digit of the integer
      return n # returns single digits as final outcome  
   else:
      end_digit = n % 10 # records the last digit of the integer
      digitalSum(n // 10) # takes off the last digit of the integer and calls function on what's left
   dig_sum_counter += end_digit # keeps a running total of the digital sum
   return dig_sum_counter