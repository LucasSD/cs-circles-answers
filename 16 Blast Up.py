def countup(n):
    if n == 1: print('Blastoff!') # base case
    else: countup(n - 1) # calls function again but new frame
    print(n) # Python exits current function and returns to the function which called it, printing n each time