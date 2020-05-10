
DEBUG = True
N = int(input())

# if N == 1:
#     print(1)
#     exit()

divisors = []

tmp = N
for i in range(2, int(N**0.5)+1):
    while tmp % i == 0:
        tmp //= i
        divisors.append(i)
if tmp != 1:
    divisors.append(tmp)

if DEBUG:
    print(divisors)

A = 1
B = 1
while divisors:
    x = divisors.pop()
    if A > B:
        B *= x
    else:
        A *= x
    if DEBUG:
        print("A: {}, B: {}, x: {}".format(A, B, x))

if DEBUG:
    print("A: {}, B: {}".format(A, B))

print(max(len(str(A)), len(str(B))))
