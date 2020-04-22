DEBUG = False

S = input()
count = 1
nums_RL = []
pre_char = S[0]
for i in range(1, len(S)):
    next_char = S[i]
    if pre_char != next_char:
        nums_RL.append(count)
        count = 0
    pre_char = next_char
    count += 1
nums_RL.append(count)
if DEBUG:
    print("nums_RL: {}".format(nums_RL))

ans = [0] * len(S)
p = 0
for i in range(len(nums_RL)//2):
    num_R = nums_RL[2*i]
    num_L = nums_RL[2*i+1]
    if DEBUG:
        print("p: {}, num_R: {}, num_L: {}".format(p, num_R, num_L))
    p += num_R
    if (num_R + num_L) % 2 == 0:
        ans[p-1] = (num_R + num_L) // 2
        ans[p] = (num_R + num_L) // 2
    else:
        ans[p-1] = num_L // 2 + (num_R + 1) // 2
        ans[p] = num_R // 2 + (num_L + 1) // 2
    p += num_L
    if DEBUG:
        print("ans: {}".format(ans))
print(*ans)
