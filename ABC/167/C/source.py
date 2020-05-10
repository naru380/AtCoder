DEBUG = False

N, M, X = map(int, input().split())
A = []
C = []
for _ in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1::])

if DEBUG:
    print(A)
    print(C)

max_money = 10**5 * N + 1
ans_money = max_money
# ans_algorythm = None
for i in range(2**N):
    bit = bin(i)[2::]
    bit = bit.zfill(N)
    if DEBUG:
        print("i: {}, bit: {}".format(i, bit))
    tmp_money = 0
    tmp_algorythm = [0] * M
    for j, b in enumerate(bit):
        if b == '1':
            tmp_money += C[j]
            for k, c in enumerate(A[j]):
                tmp_algorythm[k] += c
    if DEBUG:
        print("tmp_money: {}, tmp_algorythm: {}".format(tmp_money, tmp_algorythm))
    if len(list(filter(lambda x: x < X, tmp_algorythm))) == 0:
        ans_money = min(tmp_money, ans_money)
        if DEBUG:
            print("ans_money: {}".format(ans_money))
        # break

if ans_money == max_money:
    print(-1)
else:
    print(ans_money)
