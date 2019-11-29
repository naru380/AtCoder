K, S = list(map(int, input().split()))

ans = 0
for x in range(K+1):
    n = 0
    if S < x:
        break
    for y in range(K+1):
        n = S - (x + y)
        if 0 <= n <= K:
            ans += 1

print(ans)
