import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * (math.factorial(n - r)))

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    B = A[:i] + A[i+1:]
    ans = 0
    for c in set(B):
        find = len(list(filter(lambda x: x == c, B)))
        # print("c:{}, find:{}".format(c, find))
        if find <= 1:
            ans += 0
        else:
            ans += comb(find, 2)
    print(ans)
