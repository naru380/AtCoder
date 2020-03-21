H, W = map(int, input().split())
S = [input() for _ in range(H)]

dp = [[float('inf') for _ in range(W)] for _ in range(H)]

if S[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(1, W):
    if S[0][i] == '.':
        dp[0][i] = dp[0][i-1]
    else:
        if S[0][i-1] == '.':
            dp[0][i] = dp[0][i-1] + 1
        else:
            dp[0][i] = dp[0][i-1]

for j in range(1, H):
    if S[j][0] == '.':
        dp[j][0] = dp[j-1][0]
    else:
        if S[j-1][0] == '.':
            dp[j][0] = dp[j-1][0] + 1
        else:
            dp[j][0] = dp[j-1][0]

for j in range(1, H):
    for i in range(1, W):
        if S[j][i-1] == '.' and S[j][i] == '#':
            dp[j][i] = min(dp[j][i], dp[j][i-1] + 1)
        else:
            dp[j][i] = min(dp[j][i], dp[j][i-1])
        if S[j-1][i] == '.' and S[j][i] == '#':
            dp[j][i] = min(dp[j][i], dp[j-1][i] + 1)
        else:
            dp[j][i] = min(dp[j][i], dp[j-1][i])

print(dp[H-1][W-1])
