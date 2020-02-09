from collections import deque

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
perm = deque([(P[i]+1)/2.0 for i in range(K-1)])

for i in range(K-1, N):
    perm.append((P[i]+1)/2.0)
    if ans < sum(perm):
        ans = sum(perm)
    perm.popleft()

print(ans)
