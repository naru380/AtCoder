N, A = list(map(int, input().split()))
x = list(map(int, input().split()))

X = max(max(x), A)

dp = [[[0 for _ in range(N*X+1)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(1, N+1):
    for j in range(N+1):
        for k in range(N*X+1):
            if i >= 1 and k < x[i-1]:
                dp[i][j][k] = dp[i-1][j][k]
            elif i >= 1 and k >= 1 and k >= x[i-1]:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-x[i-1]]
            else:
                dp[i][j][k] = 0

ans = 0
for i in range(1, N+1):
    ans += dp[N][i][i*A]

print(ans)
