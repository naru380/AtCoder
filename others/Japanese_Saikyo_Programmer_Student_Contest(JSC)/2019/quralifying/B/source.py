import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

# print(A * K)

ans = 0
meets = [0] * N
for i in range(N):
    for j in range(N):
        ans += int(i < j and A[i] > A[j])
        meets[i] += int(A[i] > A[j])
ans *= K
# print(meets)

ans += sum(meets) * K * (K - 1) // 2

print(ans % MOD)
