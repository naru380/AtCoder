n, a, b = [int(i) for i in input().split(' ')]

s = 0
for i in range(1, n+1):
    if a <= sum(list(map(int, str(i)))) <= b:
        s += i

print(s)
