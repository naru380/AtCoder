# scipy.ndimage.morphology.binary_dilation
# や
# scipy.ndimage.morphology.distance_transform_cdt
# で簡単に実現できるらしい

# PyPy3でAC
import sys
from collections import deque
input = sys.stdin.readline

# ver1
# H, W = map(int, input().split())
#
# m = [[0 for _ in range(W)] for _ in range(H)]
# root = []
# for i in range(H):
#     # m.append(list(map(lambda x: 0 if x=="#" else 1, input()))）
#     for j, c in enumerate(input()):
#         if c == "#":
#             m[i][j] = 1
#             root.append((i, j))
#
# print(m)
# print(root)
#
# queue = deque(root)
# visited = deque(root)
# visited_extend = visited.extend
# ans = 0
# while len(visited) < H*W:
#     # print(visited)
#     ans += 1
#     new_queue = deque([])
#     while queue:
#         p = queue.popleft()
#         for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
#             next_p = (p[0] + i, p[1] + j)
#             if (0 <= next_p[0] < H) and (0 <= next_p[1] < W):
#                 if not m[next_p[0]][next_p[1]]:
#                     m[next_p[0]][next_p[1]] = 1
#                     new_queue.append(next_p)
#     visited_extend(new_queue)
#     queue = new_queue
# print(ans)

# ver2: 定数倍オーダ高速化
def main():
    H, W = map(int, input().split())

    m = [list(map(lambda x: 1 if x=="#" else 0, input())) for _ in range(H)]
    black = [(i, j, 0) for i in range(H) for j in range(W) if m[i][j] == 1]

    # print(m)
    # print(black)

    queue = deque(black)
    queue_append = queue.append
    ans = 0
    while queue:
        p = queue.popleft()
        if ans < p[2]:
            ans += 1
        for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            next_p = (p[0] + i, p[1] + j)
            if (0 <= next_p[0] < H) and (0 <= next_p[1] < W):
                if not m[next_p[0]][next_p[1]]:
                    m[next_p[0]][next_p[1]] = 1
                    queue_append((next_p[0], next_p[1], ans+1))
    print(ans)

if __name__ == "__main__":
    main()
