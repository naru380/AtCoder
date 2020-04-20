S = list(input())

blacks = []
for i in range(len(S)):
    if S[i] == "B":
        blacks.append(i)

# print(blacks)

for i in range(len(blacks)):
    blacks[len(blacks) - i - 1] = len(S) - i - 1 - blacks[len(blacks) - i - 1]

print(sum(blacks))
