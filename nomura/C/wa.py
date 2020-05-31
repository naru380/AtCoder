DEBUG = False

N = int(input())
A = [int(i) for i in input().split()]

if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
else:
    ranges = []
    pre_range = []
    for i in range(len(A)-2, -1, -1):
        if i == (len(A)-2):
            min_val = (A[i+1] + 1) // 2 + A[i]
            max_val = A[i+1] + A[i]
        else:
            pre_min_val, pre_max_val = pre_range
            min_val = (pre_min_val + 1) // 2 + A[i]
            max_val = pre_max_val + A[i]
        ranges.append([min_val, max_val])
        pre_range = [min_val, max_val]
        if DEBUG:
            print("i: {}, min_val: {}, max_val: {}".format(i, min_val, max_val))
    ranges = ranges[::-1]
    if DEBUG:
        print("ranges: {}".format(ranges))
    if 1 in [i for i in range(ranges[0][0], ranges[0][1])]:
        list_num_nodes = []
        list_num_nodes.append(1)
        pre_num_nodes = 1
        for i in range(1, len(ranges)):
            min_val, max_val = ranges[i]
            if DEBUG:
                print("i: {}, max_val: {}".format(i, max_val))
                print("num_nodes: {}".format(num_nodes))
            num_nodes = min((pre_num_nodes-A[i-1])*2, max_val)
            list_num_nodes.append(num_nodes)
            pre_num_nodes = num_nodes
            if num_nodes < pre_min_val:
                print(-1)
                exit(0)
        list_num_nodes.append(A[-1])
        if DEBUG:
            print("list_num_nodes: {}".format(list_num_nodes))
        print(sum(list_num_nodes))
    else:
        print(-1)
