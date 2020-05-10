DEBUG = False

N = int(input())
A = [int(i) for i in input().split()]

index_min_abs_val = N-1
flag_zero = not A[N-1]
if DEBUG:
    print("index_max_abs_val: {}, flag_zero: {}".format(index_min_abs_val, flag_zero))
for i in range(N-1):
    if not A[i]:
        flag_zero = True
    if abs(A[index_min_abs_val]) > abs(A[i]):
        index_min_abs_val = i
    if A[i] < 0:
        A[i] *= -1
        A[i+1] *= -1
    if DEBUG:
        print("i: {}, A: {}".format(i, A))
        print("index_max_abs_val: {}, flag_zero: {}".format(index_min_abs_val, flag_zero))

if flag_zero:
    A[N-1] = abs(A[N-1])
elif A[N-1] < 0:
    A[N-1] *= -1
    A[index_min_abs_val] *= -1

if DEBUG:
    print("A: {}".format(A))
print(sum(A))
