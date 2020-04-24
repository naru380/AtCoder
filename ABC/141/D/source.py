import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
A = []
for i in input().split():
    heappush(A, -1 * int(i))
# print(A)

for _ in range(M):
    val = heappop(A)
    if val == 0:
        break
    heappush(A, (val+1)//2)

print(-1 * sum(A))
