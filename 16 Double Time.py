def countdownBy2(n):
    if n <= 0: print('Blastoff!') # base case
    else:
      print(n)
      countdownBy2(n - 2) # decreases in increments of 2