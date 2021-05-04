def lowerChar(char):  #define the function which converts upper case...
    if char >= 'A' and char <= 'Z': # ...using string comparison...
        char = chr(ord(char) + 32) #...and the ASCII table
    return char

def lowerString(string): #define a function which calls lower_char for each position of the string
    result = '' #set an empty string
    for i in range(0, len(string)): #for each position of the string
        result = result + lowerChar(string[i]) #keep adding on the next part of the string   
    return result
    