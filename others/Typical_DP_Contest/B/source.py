DEBUG = False

A, B = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

# 後ろから解くことで部分問題に分けることができる
# dp[i][j] は A'=A[i:] と B'=B[j:] の部分問題において先行が獲得できる最高値
# 例えば、A=[1,2,3], B=[4,5,6] が元問題とすれば
# A'=[2,3], B'=[6] が部分問題:dp[1,2]
# ただし、元問題の順番を部分問題が引き継ぐ
# 上の例なら、dp[1,2]は元問題の後攻が先行となっている

dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

dp[len(A)][len(B)] = 0

# dp[i][j] := 左の山が i 個, 右の山が j このこっている状態からスタートするときの先手の取るものの価値の和
for i in range(len(A), -1, -1):
    for j in  range(len(B), -1, -1):
        if i == len(A) and j == len(B):
            continue
        if DEBUG:
            print("i: {}, j: {}".format(i, j))
        if (i + j) % 2 == 0:
            if i == len(A):
                dp[i][j] = dp[i][j+1]+B[j]
            elif j == len(B):
                dp[i][j] = dp[i+1][j]+A[i]
            else:
                dp[i][j] = max(dp[i+1][j]+A[i], dp[i][j+1]+B[j])
        else:
            if i == len(A):
                dp[i][j] = dp[i][j+1]
            elif j == len(B):
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = min(dp[i][j+1], dp[i+1][j])
        if DEBUG:
            print(*dp, sep="\n")
            print("---")

print(dp[0][0])
