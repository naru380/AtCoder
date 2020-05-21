n = int(input())
A = [int(a) for a in input().split()]

max_val = max(A)
mid_val = max_val - max_val//2

# print("max_val: {}, mid_val: {}".format(max_val, mid_val))

m = 0
for a in A:
    # print(abs(a - mid_val))
    # print(abs(m - mid_val))
    if abs(a - mid_val) < abs(m - mid_val):
        m = a
    # print("m: {}".format(m))

print("{} {}".format(max_val, m))
