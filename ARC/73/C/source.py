N, T = map(int, input().split())

t = list(map(int, input().split()))

diff = []

for i in range(N - 1):
    diff.append(t[i+1] - t[i])

# print(diff)

shower_time = list(map(lambda x: T if T < x else x, diff))
ans = sum(shower_time) + T

print(ans)
