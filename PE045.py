"""
Project Euler Problem #45
==========================

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle     T[n]=n(n+1)/2   1, 3, 6, 10, 15, ...
Pentagonal   P[n]=n(3n-1)/2  1, 5, 12, 22, 35, ...
Hexagonal    H[n]=n(2n-1)    1, 6, 15, 28, 45, ...

It can be verified that T[285] = P[165] = H[143] = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

start, stop = 286, 1000
while True:
    triangles    = [(n*(n+1))/2 for n in range(start, stop)]
    pentagonals  = [(n*(3*n-1))/2 for n in range(start, stop)]
    hexagonals   = [(n*(2*n-1)) for n in range(start, stop)]
	
    intersection = set.intersection(*[set((triangles)), 
						set((pentagonals)), set((hexagonals))])
	
    if intersection:
        print list(intersection)[0]
        break 
	
    start, stop = stop, stop*10
