N, X, Y = map(int, input().split())

# distの計算式で-1しているとTLE
X -= 1
Y -= 1

ans = [0] * (N - 1)
for i in range(N):
    for j in range(i + 1, N):
        dist = min(abs(i - j), abs(X - i) + abs(Y - j) + 1, abs(Y - i) + abs(X - j) + 1)
        ans[dist - 1] += 1
        # print("i:{}, j:{}, dist:{}".format(i, j, dist))
for k in ans:
    print(k)
