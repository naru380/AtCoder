N, K, S = map(int, input().split())

ans = []

for i in range(N):
    if i < K:
        ans.append(str(S))
    else:
        ans.append(str(((S % 10**9) + 1)))
        # if S == 10 ** 9:
        #     ans.append(str(1))
        # else:
        #     ans.append(str(S+1))

print(" ".join(ans))
