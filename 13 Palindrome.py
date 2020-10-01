def isPalindrome(string):
   reverse_string = string[len(string)::-1] #reverse the string
   if string == reverse_string: answer = True # palindrome
   else: answer = False #not palindrome
   return answer