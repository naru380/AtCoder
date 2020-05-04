import math

DEBUG = False

A, B, N = map(int, input().split())

if DEBUG:
    ans = 0
    for x in range(1, N+1):
        term1 = math.floor(A*x/B)
        term2 = A * math.floor(x/B)
        temp = term1 - term2
        print("x: {}, temp: {}, term1: {}, term2: {}".format(x, temp, term1, term2))
        ans = max(ans, temp)
    print(ans)

print(math.floor(A*min(B-1, N)/B)-A*math.floor(min(B-1, N)/B))
