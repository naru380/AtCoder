K = int(input())
A, B = map(int, input().split())

flag = False
for i in range(K, 1001, K):
    if A <= i <= B:
        flag = True
        break

if flag:
    print('OK')
else:
    print('NG')
