import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

h, w, a, b = list(map(int, input().split()))

ans = 0

for i in range(w-b):
    if (i == 0):
        ans += comb(h-a-1+b+i, b+i) * comb(a+w-1-b-i, a)
    else:
        ans += (comb(h-a-1+b+i, b+i) - comb(h-a-1+b+i-1, b+i-1)) * comb(a+w-1-b-i, a)

print(ans % (10**9 + 7))
