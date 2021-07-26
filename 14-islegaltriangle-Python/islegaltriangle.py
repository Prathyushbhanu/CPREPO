# islegaltriangle(s1, s2, s3)
# Write the function islegaltriangle(s1, s2, s3) that takes three int or float values representing
# the lengths of the sides of a triangle, and returns True if such a triangle exists and False
# otherwise. Note from the triangle inequality that the sum of each two sides must be greater
# than the third side, and further note that all sides of a legal triangle must be positive. Hint:
# how can you determine the longest side, and how might that help?

def trianglearea(s1, s2, s3):
    
	s=(s1+s2+s3)/2	
	b=s-s1
	c=s-s2
	d=s-s3
	e=(s*b*c*d)**0.5
	# print(e)
	# b=a**0.5