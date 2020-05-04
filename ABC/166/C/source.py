N, M = map(int, input().split())
# obs = []
H = [int(i) for i in input().split()]
H = [0] + H
bgs = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    bgs[A].append(B)
    bgs[B].append(A)

# print(H)
# print(bgs)

ans = 0
for i, bg in enumerate(bgs):
    if i == 0:
        continue
    flag = True
    for ob in bg:
        if H[i] <= H[ob]:
            flag = False
            break
    if flag or len(bg) == 0:
        # print(i)
        ans += 1

print(ans)
