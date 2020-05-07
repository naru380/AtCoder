N = int(input())
S = list(input())

# 暗証番号は 000-999 の最大1000種類

ans = 0
for i in range(1000):
    v = str(i).zfill(3)
    # print(v)
    n = 0
    f = [False] * N
    for j in range(len(S)):
        if v[n] == S[j]:
            n += 1
        if n >= 3:
            # print(v)
            ans += 1
            break

print(ans)
