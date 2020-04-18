S = input()
K = int(input())

length = len(S)

num_fixed = 0
pre_char = ''
count = 0
for i in range(length):
    now_char = S[i]
    if pre_char != now_char:
        num_fixed += count//2
        count = 0
    count += 1
    pre_char = now_char
    # print("pre_char:{}, now_char:{}, count:{}".format(pre_char, now_char, count))
num_fixed += count//2

# print(num_fixed)

if S[0] == S[length - 1]:
    head_length = 1
    head_char = S[0]
    for i in range(1, length):
        now_char = S[i]
        if now_char != head_char:
            break
        head_length += 1
    tail_length = 1
    tail_char = S[length - 1]
    for i in range(1, length):
        now_char = S[length - 1 - i]
        if now_char != tail_char:
            break
        tail_length += 1
    if length == head_length == tail_length:
        ans = length * K // 2
    else:
        ans = K * num_fixed - (K - 1) * (head_length // 2 + tail_length // 2 - (head_length + tail_length) // 2)
else:
    ans = num_fixed * K

print(ans)
