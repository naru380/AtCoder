A11, A12, A13 = map(int, input().split())
A21, A22, A23 = map(int, input().split())
A31, A32, A33 = map(int, input().split())
A = [A11, A12, A13, A21, A22, A23, A31, A32, A33]
bingo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
N = int(input())
B = []
for _ in range(N):
    B.append(int(input()))

for i, b in enumerate(B):
    for j, a in enumerate(A):
        if a == b:
            bingo[j] = 1

if (bingo[0] == bingo[1] == [2] == 1) or (bingo[3] == bingo[4] == bingo[5] == 1) or (bingo[6] == bingo[7] == bingo[8] == 1) or (bingo[0] == bingo[3] == bingo[6] == 1) or (bingo[1] == bingo[4] == bingo[7] == 1) or (bingo[2] == bingo[5] == bingo[8] == 1) or (bingo[0] == bingo[4] == bingo[8] == 1) or (bingo[2] == bingo[4] == bingo[6] == 1):
    print('Yes')
else:
    print('No')
