width = int(input()) #THE CODE BELOW ONLY WORKS WITH MULTIPLE LINES OF INPUT
while True: #keep repeating the steps below
    string = input()
    if string == 'END': break #stop while loop when input is END
    diff = width - len(string)      
    if diff % 2 == 0: # if the diff is an even number
        print('.' * (diff // 2) + string + '.' * (diff // 2)) #print dots on both sides
    else: # if the diff is an odd number
        print('.' * (diff // 2) + '.' + string + '.' * (diff // 2)) #print dots on both sides but add an extra dot 