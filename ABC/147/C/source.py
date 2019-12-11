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
    bin_i = format(i, '0' + str(N) + 'b')
    flag = True
    for j in range(N):
        for k in range(A[j]):
            if bin_i[j] == '1' and xy[j][k][1] != int(bin_i[xy[j][k][0]-1]):
                flag = False
                break
        if not flag:
            break

    if flag is True:
        honest = bin_i.count('1')
        if honest > ans:
            ans = honest

print(ans)
