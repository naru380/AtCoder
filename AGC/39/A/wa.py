S = input()
K = int(input())

length = len(S)
num_correct = 0
pre_char = S[0]
correct_S = S[0]
for i in range(1, length):
    now_char = S[i]
    if pre_char == now_char:
        num_correct += 1
        pre_char = '-'
    else:
        pre_char = now_char
    correct_S += pre_char
# print("num_correct:{}".format(num_correct))
# print("correct_S:{}".format(correct_S))

if length == 1:
    ans = K // 2
else:
    if S[0] == S[length-1]:
        # ans = num_correct * K + (K - 1)
        # S = aabaaa, K = 2 の場合, ans = 5, correct_S = a_ba_a となってしまう
        # 最短は, correct_S = _aba_a で ans = 4
        # S = aaabaa, K = 2 の場合, ans = 4, correct_S = a_aba_ となり最短っぽい
        # => S[0] == S[len(S)-1] なら, 先頭と最後尾で連続するそれぞれの文字数で計算が必要
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
        # print("head_length: {}, tail_length: {}".format(head_length, tail_length))
        if length == head_length == tail_length:
            # print("length == head_length == tail_length")
            ans = num_correct * K
        else:
            # print("not length == head_length == tail_length")
            ans = K * num_correct - (K - 1) * (head_length // 2 + tail_length // 2 - (head_length + tail_length) // 2)
    else:
        ans = num_correct * K
# print(correct_S*K)
print(ans)
