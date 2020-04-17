import fractions
from functools import reduce
import itertools
import math

def gcd(*numbers):
    return reduce(math.gcd, numbers)

K = int(input())

if K == 1:
    ans = 1
elif K == 2:
    ans = 9
else:
    ans = 0
    for i in range(1, K+1):
        ans += i
        for j in range(i+1, K+1):
            ans += gcd(i, j) * 6
            for k in range(j+1, K+1):
                ans += gcd(i, j, k) * 6

print(ans)
