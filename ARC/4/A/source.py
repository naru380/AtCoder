N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

def calc_dist(p0, p1):
    return ((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2) ** (1/2)


ans = calc_dist(p[0], p[1])
for i in range(len(p)):
    for j in range(i, len(p)-1):
        dist = calc_dist(p[i], p[j+1])
        if ans < dist:
            ans = dist

print(ans)
