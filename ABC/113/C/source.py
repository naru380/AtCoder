DEBUG = False

N, M = map(int, input().split())
iPY = []
for i in range(M):
    P, Y = map(int, input().split())
    iPY.append([i, P, Y])

if DEBUG:
    print(iPY)

sorted_iPY = sorted(iPY, key=lambda x: x[2])

if DEBUG:
    print(sorted_iPY)

counts = {}

for n, ipy in enumerate(sorted_iPY):
    i, p, y = ipy
    if p not in counts:
        counts[p] = 1
    else:
        counts[p] += 1
    if DEBUG:
        print(counts)
    sorted_iPY[n].append("{:0=6}".format(p) +  "{:0=6}".format(counts[p]))

if DEBUG:
    print(sorted_iPY)

restored_iPY = sorted(iPY, key=lambda x: x[0])

if DEBUG:
    print(restored_iPY)

for i in range(M):
    print(restored_iPY[i][3])
