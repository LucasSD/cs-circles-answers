word_list = [] # create empty list
while True:
   line = input().lower() # take the input string and convert to lower case
   if line.count('###') == 1: break #exit while loop if it's the last line (line contains '###')
   word_list.extend(line.split()) # add the list of new words onto the end of word_list
   
frequency = [] # create empty list
for i in word_list: #for every entry in word list
   frequency.append(word_list.count(i)) # build a list of the frequency of each word, matching its position in word_list
print(word_list[(frequency.index(max(frequency)))])   # print the word_list entry which occurs at the position of the highest frequency word