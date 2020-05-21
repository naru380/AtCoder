A, B, C = map(int, input().split())
if A == B == C and A % 2 == 0:
  print(-1)
else:
  count = 0
  while 0 == A % 2 == B % 2 == C % 2:
    _A = (B + C) // 2
    _B = (C + A) // 2
    _C = (A + B) // 2
    A = _A
    B = _B
    C = _C
    count += 1
    # print("A: {}, B: {}, C: {}".format(A, B, C))
  print(count)
