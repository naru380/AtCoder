N = int(input())
W = [int(input()) for _ in range(N)]
# print("W: {}".format(W))

ans = [W[0]]
for i in range(1, N):
    # print("ans: {}".format(ans))
    if max(ans) < W[i]:
        ans.append(W[i])
        ans = sorted(ans)
    else:
        for j, v in enumerate(ans):
            if W[i] <= v:
                ans[j] = W[i]
                break
print(len(ans))
