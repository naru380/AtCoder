from collections import deque
import sys
import time
def input(): return sys.stdin.readline().strip()

DEBUG = True

N, M, K = map(int, input().split())

friend_matrix = [[0] * N for _ in range(N)]
block_matrix = [[0] * N for _ in range(N)]

num_connected_friends = [0] * N
num_connected_blocks = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    friend_matrix[A-1][B-1] = 1
    friend_matrix[B-1][A-1] = 1
    num_connected_friends[A-1] += 1
    num_connected_friends[B-1] += 1

for _ in range(K):
    C, D = map(int, input().split())
    block_matrix[C-1][D-1] = 1
    block_matrix[D-1][C-1] = 1

if DEBUG:
    # print("friend_matrix: {}".format(friend_matrix))
    print("friend_matrix:")
    for row in friend_matrix:
        print(row)
    # print("block_matrix: {}".format(block_matrix))
    print("block_matrix:")
    for row in block_matrix:
        print(row)
    print("enter!!")

count = 0
labels = [-1] * N
graph_sizes = []
total_iteration = 0
for n in range(N):
    if DEBUG:
        print("root_node: {}, count: {}".format(n+1, count))
    if labels[n-1] == -1:
        queue = deque([n+1])
        labels[n] = count
        size = 0
        while queue:
            if DEBUG:
                print("queue:{}".format(queue))
            node = queue.popleft()
            size += 1
            if DEBUG:
                print("node:{}".format(node))
            for i in range(N):
                total_iteration += 1
                if labels[i] == -1 and friend_matrix[node-1][i] == 1:
                    labels[i] = count
                    queue.append(i+1)
                if labels[node-1] == labels[i]:
                    num_connected_blocks[node-1] += block_matrix[node-1][i]
                    num_connected_blocks[i] += block_matrix[node-1][i]
            if DEBUG:
                print("labels: {}".format(labels))
            # time.sleep(0.2)
        count += 1
        graph_sizes.append(size)
if DEBUG:
    print("total_iteration: {}".format(total_iteration))
    print("labels: {}".format(labels))
    print("graph_sizes: {}".format(graph_sizes))
    print("num_connected_friends: {}".format(num_connected_friends))
    print("num_connected_blocks: {}".format(num_connected_blocks))

frind_candidate = [0] * N
for n in range(N):
    # num_block = sum(block_matrix[n])
    # num_block = 0
    # for i in range(N):
    #     if block_matrix[n][i] == 1 and labels[n] == labels[i]:
    #         num_block += 1
    num_block = num_connected_blocks[n]
    # num_frined = sum(friend_matrix[n])
    num_frined = num_connected_friends[n]
    if DEBUG:
        print("node: {}, num_frined: {}, num_block: {}".format(n+1, num_frined, num_block))
    frind_candidate[n] = graph_sizes[labels[n]] - num_frined - num_block - 1
frind_candidate = list(map(str, frind_candidate))
# print(" ".join(frind_candidate))
print(*frind_candidate)
