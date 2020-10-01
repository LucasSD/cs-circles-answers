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
  visited = [False] * len(prog) # create a list as long as the BASIC programme to track when a line has been visited already
  while True:
    if location == len(prog)-1: return "success" # if you reach the final line of the BASIC program
    if visited[location] == True: return 'infinite loop' # if this line of BASIC code has been visited before
    list_of_string = prog[location].split() #remove spaces from the string at the position of location, and put each word into a list
    del visited[location] # remove this list entry
    visited.insert(location, True) # insert this entry into the list
    T = list_of_string[len(list_of_string) - 1] # initialise T as the target (final string) in list_of_string
    location = findLine(prog, T) # find the line with the desired location (first part) by calling findLine function

print(execute(getBASIC()))