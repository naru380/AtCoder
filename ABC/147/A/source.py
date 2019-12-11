A = list(map(int, input().split()))

ans = sum(A)

if ans >= 22:
    print('bust')
else:
    print('win')
