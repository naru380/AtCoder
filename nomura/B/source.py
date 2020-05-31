T = input()
T = list(T)

for i in range(len(T)):
    if T[i] == "?":
        T[i] = "D"

print(*T, sep="")
