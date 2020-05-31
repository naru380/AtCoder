R, G, B, N = map(int, input().split())
# print("(N,R,G,B)=({},{},{},{})".format(N,R,G,B))

ans = 0
for i in range(N+1):
    if R*i > N:
        break
    for j in range(N+1):
        tmp = R*i + G*j
        # print("i={},j={},tmp={}".format(i,j,tmp))
        if tmp > N:
            break
        if (N-tmp)%B == 0:
            ans += 1
            # print("(i,j,k)=({},{},{})".format(i,j,(N-tmp)//B))
print(ans)
