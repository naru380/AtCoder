N = int(input())
R = []
for _ in range(N):
    X, L = map(int, input().split())
    R.append([X-L, X+L])

R = sorted(R, key=lambda x: x[1])

ans = 1
p = R[0][1]
for i in range(1, N):
    if p <= R[i][0]:
        ans += 1
        p = R[i][1]

print(ans)
