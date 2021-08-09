# Write the function fun_threelines_area(d1, d2, d3) that takes length of 3 sides to find the area of a triangle(return an int) given its side lengths.
import math
def fun_threelines_area(a, b, c):
   s = (a+b+c)/2
   d = s*(s-a)*(s-b)*(s-c)
   area = int(math.sqrt(d))
   return area  
