from collections import deque
import sys
import time
def input(): return sys.stdin.readline().strip()

DEBUG = False

N, M, K = map(int, input().split())

friend_relations = [[] for _ in range(N+1)]
block_relations = [[] for _ in range(N+1)]

num_connected_friends = [0] * (N+1)
num_connected_blocks = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    friend_relations[A].append(B)
    friend_relations[B].append(A)

for _ in range(K):
    C, D = map(int, input().split())
    block_relations[C].append(D)
    block_relations[D].append(C)

if DEBUG:
    print("friend_relations:")
    for i, row in enumerate(friend_relations):
        print("node: {}, relation: {}".format(i, row))
    print("block_matrix:")
    for i, row in enumerate(block_relations):
        print("node: {}, relation: {}".format(i, row))

count = 0
labels = [-1] * (N+1)
graph_sizes = []
total_iteration = 0
for n in range(1, N+1):
    if DEBUG:
        print("root_node: {}, count: {}".format(n, count))
    if labels[n] == -1:
        queue = deque([n])
        labels[n] = count
        size = 0
        while queue:
            if DEBUG:
                print("queue:{}".format(queue))
            node = queue.popleft()
            size += 1
            if DEBUG:
                print("node:{}".format(node))
            for next_node in friend_relations[node]:
                total_iteration += 1
                if labels[next_node] == -1:
                    labels[next_node] = count
                    queue.append(next_node)
            if DEBUG:
                print("labels: {}".format(labels))
            # time.sleep(0.2)
        count += 1
        graph_sizes.append(size)
if DEBUG:
    print("total_iteration: {}".format(total_iteration))
    print("labels: {}".format(labels))
    print("graph_sizes: {}".format(graph_sizes))

friend_candidate = [0] * (N+1)
for n in range(1, N+1):
    num_block = sum([1 for i in block_relations[n] if labels[n] == labels[i]])
    num_frined = len(friend_relations[n])
    if DEBUG:
        print("node: {}, num_frined: {}, num_block: {}".format(n+1, num_frined, num_block))
    friend_candidate[n] = graph_sizes[labels[n]] - num_frined - num_block - 1

print(*friend_candidate[1:])
