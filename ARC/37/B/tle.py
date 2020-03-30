import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())

m = [[0 for _ in range(W)] for _ in range(H)]
root = []
for i in range(H):
    # m.append(list(map(lambda x: 0 if x=="#" else 1, input()))）
    for j, c in enumerate(input()):
        if c == "#":
            m[i][j] = 1
            root.append((i, j))

# print(m)
# print(root)

queue = deque(root)
def bfs():
    new_queue = deque([])
    while queue:
        p = queue.popleft()
        for i, j in ([-1, 0], [1, 0], [0, 1], [0, -1]):
            next_p = [p[0] + i, p[1] + j]
            if (0 <= next_p[0] < H) and (0 <= next_p[1] < W):
                if not m[next_p[0]][next_p[1]]:
                    m[next_p[0]][next_p[1]] = 1
                    new_queue.append(next_p)
    return new_queue

ans = 0
if len(root) != H*W:
    while queue:
        # print(queue)
        # print(m)
        queue = bfs()
        ans += 1
    ans -= 1

print(ans)
