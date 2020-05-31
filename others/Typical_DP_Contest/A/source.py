import copy

N = int(input())
P = list(map(int, input().split()))

# dp = [0] * 10001
dp = [False] * (max(P) * N + 1)
dp[0] = True

max_val = 0
for v in P:
    tmp_dp = copy.deepcopy(dp)
    # print("v: {}".format(v))
    for i in range(max_val+1):
        if tmp_dp[i]:
            dp[v+i] = True
    dp[v] = True
    max_val += v

# print(dp)
print(dp.count(True))
