N , M = map(int, input().split())

ab = []
for _ in range(N):
    a, b = map(int, input().split())
    ab.append([a, b])

cd = []
for _ in range(M):
    c, d = map(int, input().split())
    cd.append([c, d])

# print(ab)
# print(cd)

for i in range(N):
    a, b = ab[i]
    tmp = float('inf')
    p = -1
    for j in range(M):
        c, d = cd[j]
        dist = abs(a-c)+abs(b-d)
        if tmp > dist:
            tmp = dist
            p = j+1
    print(p)
