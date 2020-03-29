K, N = map(int, input().split())
A = list(map(int, input().split()))

m = A[N-1] - A[0]

for i in range(N - 1):
    n = (K - A[i+1]) + A[i]
    # print("i:{}, n:{}".format(i, n))

    if n < m:
        m = n

print(m)
