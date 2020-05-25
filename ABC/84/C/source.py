DEBUG = False

N = int(input())
CSF = []
for i in range(N-1):
    csf = list(map(int, input().split()))
    CSF.append(csf)

if DEBUG:
    print("CSF: {}".format(CSF))

for i in range(N-1):
    ans = 0
    for j in range(i, N-1):
        if DEBUG:
            print("i: {}, j: {}, ans: {}".format(i, j, ans))
        c, s, f = CSF[j]
        if ans < s:
            ans = s
        elif ans  % f != 0:
            ans += f - ans % f
        else:
            pass
        ans += c
    if DEBUG:
        print("i: {}, j:{}, ans:{}".format(i, j, ans))
    print(ans)
print(0)
