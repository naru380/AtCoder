import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

sorted_A = sorted(A)
num_pair = N * (N-1) / 2

B = []
for perm in list(itertools.combinations(A, 2)):
    B.append(perm[0]*perm[1])

print(sorted(B)[K-1])
