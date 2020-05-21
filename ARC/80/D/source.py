H, W = map(int, input().split())
N = int(input())
A = [int(i) for i in input().split()]

align = [(i+1) for i, a in enumerate(A) for _ in range(a)]
# print("align: {}".format(align))
count = 0
ans = []
for i in range(H):
    tmp = align[W*i:W*(i+1)]
    if i % 2 != 0:
        tmp = tmp[::-1]
    print(*tmp)
