K, S = list(map(int, input().split()))

ans = 0
for x in range(K+1):
    xyz = 0
    if S < x:
        break
    for y in range(K+1):
        if S < x+y:
            break
        for z in range(K+1):
            if x+y+z == S:
                ans += 1
            elif S < x+y+z:
                break

print(ans)
