N, K = map(int, input().split())

x = N % K

if abs(x - K) > x:
    print(x)
else:
    print(abs(x - K))
