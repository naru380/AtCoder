n = int(input())
a = list(map(int, input().split()))

ans = sum([i**2 for i in a])

for i in range(-100, 100+1):
    s = sum([(j-i)**2 for j in a])
    if ans > s:
        ans = s

print(ans)
