"""
Project Euler Problem #63
==========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

x = 0
for p in range(1, 22):
    for n in range(1, 10):
        if len(str(n**p)) == p:
            # print p, len(str(n**p)), n**p
            x+=1

print x 