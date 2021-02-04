#import the tan function and constant pi from math
from math import tan, pi 

#define the polysum function
def polysum(n, s):
   '''
   n int, number of sides
   s int or float, length of side
   '''
   # calculate the area, coerce to float
   area = 1.0 * n * s * s / (4 * tan(pi / n))
   # calculate the length of the perimiter, as float
   perimeter = 1.0 * n * s
   # return the sum of the area and sq perimiter to 4 d.p.
   return round(area + perimeter * perimeter, 4)
