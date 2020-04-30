N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

diff = N - M
for i in range(diff+1):
    for j in range(diff+1):
        flag = True
        for k in range(M):
            if not (B[k] in A[j+k][i:i+M]):
                flag = False
        if flag:
            print('Yes')
            exit(0)

print('No')
