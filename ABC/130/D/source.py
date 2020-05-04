N, K = map(int, input().split())
a = [int(i) for i in input().split()]

ans = 0
right = 0
lr_sum = 0
# 尺取り法
for left in range(N):
    while right < N and lr_sum < K:
        lr_sum += a[right]
        right += 1
        # print("l: {}, r:{}, lr_sum: {}".format(left, right, lr_sum))
    if lr_sum >= K:
        # print("left={},right={} は条件を満たす".format(left, right))
        # print("left={}の場合、{}通り".format(N-right+1))
        ans += N-right+1
    lr_sum -= a[left]

print(ans)
