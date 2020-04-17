N, M = map(int, input().split())

ans = [-1] * N
if N == 1 and M == 0:
    print(0)
    exit(0)
for _ in range(M):
    sn, cn = map(int, input().split())
    if ans[sn - 1] != -1 and ans[sn - 1] != cn:
        print(-1)
        exit(0)
    if sn == 1 and cn == 0 and N > 1:
        print(-1)
        exit(0)
    ans[sn - 1] = cn
if ans[0] == -1:
    ans[0] = 1
ans = list(map(lambda x: str(0) if x == -1 else str(x), ans))
print("".join(ans))
