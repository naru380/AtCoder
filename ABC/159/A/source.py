import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * (math.factorial(n - r)))

N, M = map(int, input().split())

ans = 0
if N >= 2:
    ans += comb(N, 2)
if M >= 2:
    ans += comb(M, 2)

print(ans)
