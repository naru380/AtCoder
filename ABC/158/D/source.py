from collections import deque

S = input()
q = int(input())

is_s0_head = True
tail = len(S)-1

queue = deque(S)

for _ in range(q):
    # print(queue)
    Q = list(input().split())
    if Q[0] == "1":
        is_s0_head = not is_s0_head
    else:
        if Q[1] == "1":
            if is_s0_head:
                queue.appendleft(Q[2])
            else:
                queue.append(Q[2])
        else:
            if is_s0_head:
                queue.append(Q[2])
            else:
                queue.appendleft(Q[2])

if is_s0_head:
    print("".join(list(queue)))
else:
    print("".join(list(queue)[::-1]))
