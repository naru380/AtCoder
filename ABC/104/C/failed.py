D, G = list(map(int, input().split()))
pc = [list(map(int, input().split())) for _ in range(D)]

for i in range(len(pc)):
    pc[i].append((100 * (i+1) * pc[i][0] + pc[i][1]) / pc[i][0])
    pc[i].append(i+1)

pc = sorted(pc, key=lambda x: x[2], reverse=True)

ans = 0
del_list = []
for i, info in enumerate(pc):
    if (100 * info[3] * info[0] + info[1]) <= G:
        G -= (100 * info[3] * info[0] + info[1])
        ans += info[0]
        del_list.append(i)
    else:
        break

print(pc)
pc = [info for i, info in enumerate(pc) if i not in del_list]

pc = sorted(pc, key=lambda x: x[3], reverse=True)

while G > 0:
    G -= 100 * pc[0][3]
    pc[0][0] -= 1
    ans += 1
    if pc[0][0] == 0:
        G -= pc[0][1]
        pc.pop(0)

print(ans)
