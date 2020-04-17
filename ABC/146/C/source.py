# import time

A, B, X = map(int, input().split())

left = 0
right = 10**9
mid = (right + left) // 2

def get_price(N):
    return A * N + B * len(str(N))

ans = 0
price = get_price(right)
if A + B > X:
    ans = left
elif price <= X:
    ans = right
else:
    while left <= right:
        # print("left:{}, mid:{}, right:{}".format(left, mid, right))
        price = get_price(mid)
        # print("price:{}".format(price))
        if price == X:
            ans = mid
            break
        elif price < X:
            left = mid+1
        else:
            right = mid-1
        ans = mid = (right + left) // 2
        # time.sleep(0.1)

print(ans)
