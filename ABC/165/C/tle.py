import itertools

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
P = [[i for i in range(1, M+1)] for _ in range(N)]

# print(R)
for comb in itertools.product(*P):
    flag = True
    p = comb[0]
    for i in comb:
        if i < p:
            flag = False
            break
        p = i

    if not flag:
        continue

    # print(comb)

    temp = 0
    for abcd in ABCD:
        a, b, c, d = abcd
        if comb[b-1] - comb[a-1] == c:
            temp += d
    if temp >= ans:
        ans = temp

print(ans)
