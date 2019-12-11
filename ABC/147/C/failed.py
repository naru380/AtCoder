N = int(input())
xy = []
A = []
for i in range(N):
    Ai = int(input())
    xyi = []
    for j in range(Ai):
        xyi.append(list(map(int, input().split())))
    A.append(Ai)
    xy.append(xyi)

ans = 0

for i in range(2**N):
    bin_i = format(i, '4b')
    flag = True
    for n, c in enumerate(bin_i):
        if c == '1':
            for j in range(N):
                for k in range(A[j]):
                    if xy[j][k][0] == n:
                        if xy[j][k][1] == 0:
                            flag = False
                            break
                if not flag:
                    break
    if flag is True:
        honest = bin_i.count('1')
        if honest > ans:
            ans = honest

print(ans)
