def distance2D(x1, y1, x2, y2): # function to find the distance between to points in 2D
   a = max(x1 - x2, x2 - x1) #find horizontal length
   b = max(y1 - y2, y2 - y1) # find vertical length
   return hypotenuse(a, b) # assign the distance between two points as the function return value