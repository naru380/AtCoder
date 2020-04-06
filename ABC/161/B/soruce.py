N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)

B = list(filter(lambda x: x >= total/(4*M), A))

if len(B) >= M:
    print('Yes')
else:
    print('No')
