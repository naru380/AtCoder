N, K = map(int, input().split())
MOD = 10**9+7

mx = [0]*(K+1)
ans = 0

for i in range(K, 0, -1):
    mx[i] = pow(K//i, N, MOD)
    for j in range(2*i, K+1, i):
        mx[i] -= mx[j]
    ans += i*mx[i]

print(ans%MOD)
