n = int(input())
s = [list(map(int, input().split(' '))) for i in range(n)]

s0 = [0, 0, 0]
for s1 in s:
    sdf = [abs(p1-p0)  for p0, p1 in zip(s0, s1)]
    tdf = sdf[0]
    dst = sdf[1] + sdf[2]
    if(dst <= sdf[0]):
        tdf %= 2
        rst = dst % 2
        if(rst == tdf):
            s0 = s1
            continue
    print('No')
    exit(0)

print('Yes')
