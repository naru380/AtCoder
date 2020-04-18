import time
N = int(input())
L = list(map(int, input().split()))

L = sorted(L)

# print(L)

# 三角形なのでa>b>cになるように選べば, a+b>cとなる
ans = 0
for i in range(N-2):
    a = L[i]
    for j in range(i+1, N-1):
        # print("i:{}, j:{}".format(i, j))
        b = L[j]
        left = j+1
        right = N-1
        c = L[N-1]
        if a+b>c:
            # print("true - k:{}".format(N-1))
            # print("num_c:{}".format())
            ans += N-j-1
        else:
            mid = right
            while left < right:
                if mid == (left+right)//2:
                    break
                mid = (left+right)//2
                # print("left:{}, mid:{}, right:{}".format(left, mid, right))
                c = L[mid]
                if a+b>c:
                    left = mid
                else:
                    right = mid
                # time.sleep(0.05)
            # print("false - k:{}".format(mid))
            if a+b>c:
                # print("a+b>c:{}".format(True))
                ans += mid - j
            else:
                # print("a+b>c:{}".format(False))
                ans += mid - j - 1
        # print("ans of ({},{}): {}".format(i,j,ans))

print(ans)
