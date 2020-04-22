L, R = map(int, input().split())
MOD = 2019
ans = L*R%MOD
for i in range(L, R):
    for j  in range(i+1, R+1):
        if ans > i*j%MOD:
            ans = i*j%MOD
        if ans == 0:
            break
    if ans == 0:
        break
print(ans)
