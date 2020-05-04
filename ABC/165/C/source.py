import itertools

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

# 重複組み合わせ: nHr = n+r-1Cr を考える
ans = 0
R = [i for i in range(1, M+1)]
# print(R)

for comb in itertools.combinations_with_replacement(R, N):
    temp = 0
    for abcd in ABCD:
        a, b, c, d = abcd
        if comb[b-1] - comb[a-1] == c:
            temp += d
    if temp >= ans:
        ans = temp

    # print("comb: {}, temp: {}, ans: {}".format(comb, temp, ans))

print(ans)
