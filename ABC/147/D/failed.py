import math

N = int(input())
A = list(map(int, input().split()))

digit = math.floor(math.log2(max(A))) + 1
bin_A = [format(Ai, '0' + str(digit) + 'b') for Ai in A]

ans = 0

for i in range(digit):
    num0 = 0
    num1 = 0
    for j in range(N):
        if bin_A[j][i] == '1':
            num1 += 1
        else:
            num0 += 1
    ans += ((num1 * num0) * (2**(digit-i-1))) % (10**9+7)

print(ans % (10**9 + 7))
