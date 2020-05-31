DEBUG = False

N = int(input())
LEAVES = [int(i) for i in input().split()]

ranges_num_nodes = [[0 for _ in range(2)] for _ in range(N + 1)]
ranges_num_nodes[N][0] = LEAVES[N]
ranges_num_nodes[N][1] = LEAVES[N]

if DEBUG:
    print("ranges_num_nodes: {}".format(ranges_num_nodes))

for depth in range(N, 0, -1):
    ranges_num_nodes[depth-1][0] = LEAVES[depth-1] + (ranges_num_nodes[depth][0] + 1) // 2
    ranges_num_nodes[depth-1][1] = LEAVES[depth-1] + ranges_num_nodes[depth][1]

if DEBUG:
    print("ranges_num_nodes: {}".format(ranges_num_nodes))

num_nodes = [0] * (N + 1)
num_nodes[0] = 1

if DEBUG:
    print("num_nodes: {}".format(num_nodes))

for depth in range(N):
    num_nodes[depth+1] = min((num_nodes[depth] - LEAVES[depth]) * 2, ranges_num_nodes[depth+1][1])

if DEBUG:
    print("num_nodes: {}".format(num_nodes))

for depth in range(N+1):
    if num_nodes[depth] < ranges_num_nodes[depth][0]:
        print(-1)
        break
else:
    print(sum(num_nodes))
