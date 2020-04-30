N, M = map(int, input().split())
A = [int(i) for i in input().split()]
BC = []
for _ in range(M):
    B, C = map(int, input().split())
    BC.append([B, C])
BC = sorted(BC, key=lambda x: x[1], reverse=True)
# print("A: {}".format(A))
# print("BC: {}".format(BC))

A_dash = []
for ij in BC:
    i, j = ij
    A_dash.extend([j]*i)
    if len(A_dash) >= N:
        break
A_dash = A_dash[:N]

A_dash.extend(A)
A_dash = sorted(A_dash, reverse=True)[:N]

print(sum(A_dash))
