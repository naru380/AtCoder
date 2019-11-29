N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = 0
for i in range(1, N+1):
    if (i > K):
        ans += Y
    else:
        ans += X

print(ans)
