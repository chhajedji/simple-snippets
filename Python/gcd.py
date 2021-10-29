#!/usr/bin/env python3

# The Euclidean algorithm is based on the following two facts:

# 1. gcd(a,0) = a
# 2. gcd(a,b) = gcd(b,r), where r is the remainder of dividing a by b

iterations = 0
def gcd(a, b):
    global iterations
    iterations += 1
    # Make a larger and b smaller one.
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

gcd (1160718174, 316258250)
print("iterations: {}".format(iterations))
