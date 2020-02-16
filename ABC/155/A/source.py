A, B, C = map(int, input().split())
f1 = f2 = f3 = 0

if A == B:
    f1 = 1
if B == C:
    f2 = 1
if C == A:
    f3 = 1

if f1+f2+f3 == 1:
    print('Yes')
else:
    print('No')
