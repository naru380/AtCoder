import sys
if sys.version_info.minor < 5:
    from fractions import gcd
else:
    from math import gcd
import math

DEBUG = False

A, B = map(int, input().split())
g = gcd(A, B)
if DEBUG:
    print("gcd(A, B): {}".format(g))

ans = [1]
i= 2
temp = g
while i <= int(-(-g**0.5//1))+1:
    if DEBUG:
        print("i: {}, g: {}".format(i, g))

    if temp % i == 0:
        if DEBUG:
            print("This is a cd of A and B.")
        ans.append(i)

    while temp % i == 0:
        temp //= i

    i += 1

if temp != 1:
    ans.append(temp)

if DEBUG:
    print(ans)

print(len(ans))
