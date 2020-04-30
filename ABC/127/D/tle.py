N, M = map(int, input().split())
A = [int(i) for i in input().split()]
min_val = sorted(A, reverse=True)[N-1]
for _ in range(M):
    B, C = map(int, input().split())
    if min_val <= C:
        A.extend([C]*B)
        A = sorted(A, reverse=True)[:N]
        min_val = A[N-1]
    # print("B: {}, C:{}".format(B, C))
    # print("A: {}".format(A))
A = sorted(A, reverse=True)
print(sum(A[:N]))
