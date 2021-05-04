num_rows=int(input())
for i in range(num_rows):
    X = 0
    for j in range(0, num_rows - i):
        X = (X*10)+1      
    print(X)