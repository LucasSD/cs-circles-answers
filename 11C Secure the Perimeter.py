def trianglePerimeter(xA, yA, xB, yB, xC, yC): # function to add three sides together for any triangle
   return distance2D(xA, yA, xB, yB) + distance2D(xA, yA, xC, yC) + distance2D(xB, yB, xC, yC)