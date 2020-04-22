N = int(input())
A = list(map(int, input().split()))

average = sum(A) // N
ans1 = 0
for i in A:
    ans1 += (i-average)**2
ans2 = 0
for i in A:
    ans2 += (i-average-1)**2
ans = min(ans1, ans2)

print(ans)
