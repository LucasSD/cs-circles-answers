needle = input()
haystack = input()
needle_first_letter = needle[0]

needle_length = len(needle)
haystack_length = len(haystack)
num_needles = 0

for i in range(haystack_length - needle_length + 1): #search only to last possible start of a needle
   if haystack[i] == needle_first_letter: # if the letter is the first letter of needle
       if haystack[i:i + needle_length] == needle: #and if that letter is the start of a needle
           num_needles = num_needles + 1
   
print(num_needles) #print number of times needle occurs in haystack