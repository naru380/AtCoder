H, W = map(int, input().split())

campus = []

campus.append("."*(W+2))
for _ in range(H):
    s = list("."+input()+".")
    campus.append(s)
campus.append("."*(W+2))

# print(campus)

flag = True
for i in range(1, H+1):
    for j in range(1, W+1):
        if campus[i][j] == "#":
            if campus[i-1][j] != "#" and campus[i+1][j] != "#" and campus[i][j-1] != "#" and campus[i][j+1] != "#":
                flag = False

if flag:
    print("Yes")
else:
    print("No")
