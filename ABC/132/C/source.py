N = int(input())
D = list(map(int, input().split()))

D = sorted(D)
left = D[N//2-1]
right = D[N//2]
# print("left: {}, right: {}".format(left, right))
print(right-left)
