import math

N = int(input())
A = list(map(int, input().split()))

ans = 0
fil = 1
for i in range(60):
    num1 = len([1 for j in range(N) if A[j] & fil])
    num0 = N - num1
    ans += (num1 * num0) * fil
    fil <<= 1

print(ans % (10 ** 9 + 7))
