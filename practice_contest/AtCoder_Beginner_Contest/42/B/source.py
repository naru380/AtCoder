n, l = list(map(int, input().split()))
s = [input() for _ in range(n)]

s.sort()

print(''.join(s))
