N, K = map(int, input().split())
P = list(map(int, input().split()))

cml_sum = [(P[0]+1)/2.0]
for i in range(1, N):
    cml_sum.append(cml_sum[i-1] + (P[i]+1)/2.0)

ans = cml_sum[K-1]
for i in range(N-K):
    target = cml_sum[i+K] - cml_sum[i]
    if ans < target:
        ans = target

print(ans)
