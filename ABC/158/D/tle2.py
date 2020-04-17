S = input()
q = int(input())

is_s0_head = True
tail = len(S)-1

for _ in range(q):
    # print(S)
    Q = list(input().split())
    if Q[0] == "1":
        is_s0_head = not is_s0_head
    else:
        if Q[1] == "1":
            if is_s0_head:
                S = Q[2] + S
            else:
                S = S + Q[2]
        else:
            if is_s0_head:
                S = S + Q[2]
            else:
                S = Q[2] + S

if is_s0_head:
    print(S)
else:
    print(S[::-1])
