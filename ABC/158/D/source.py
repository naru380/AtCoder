S = input()
q = int(input())

tail = len(S)-1

for _ in range(q):
    # print(S)
    Q = list(input().split())
    if Q[0] == "1":
        S = S[::-1]
    else:
        if Q[1] == "1":
            S = Q[2] + S
        else:
            S = S + Q[2]
print(S)
