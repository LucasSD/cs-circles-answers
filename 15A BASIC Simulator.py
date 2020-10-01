def getBASIC():
   line = input()
   list = [] # create an empty list
   while line.count('END') <= 1: # execute the while block until you reach the final line of BASIC code which contains 'END'
      
      list.append(line) # append the list of input srings
      if line.endswith('END'): #exit the while loop when you reach the final line with 'END'
         break
      line = input() # read the next line of input
      
   return list

def findLine(prog, target):
   for i in range (len(prog)): # scan forwards through each list entry
      if prog[i].startswith(target): #if string at i starts with target substring
         return i #return position i

def execute(prog):
  location = 0
  line_counter = 0 # used to determine if infinte loop
  while True:
    if location == len(prog)-1: return "success" # if you reach the final line of the BASIC program
    list_of_string = prog[location].split() # remove spaces from the string at the position of location, and put each word into a list
    T = list_of_string[len(list_of_string) - 1] # initialise T as the target (final string) in list_of_string
    location = findLine(prog, T) # find the line with the desired location (first part) by calling findLine function
    line_counter += 1 # increase counter every iteration to check for infinte loop
    if line_counter >= len(prog): return 'infinite loop' # if every line has been visited and you haven't reached final line, must be an infinite loop
      
print(execute(getBASIC()))