N = int(input())
s = []
t = []
for _ in range(N):
  tmp = int(input())
  s.append(tmp)
  if tmp % 10 != 0:
    t.append(tmp)

ans = sum(s)

if ans % 10 != 0:
  print(ans)
else:
  if not t:
    print(0)
  else:
  	print(ans - min(t))
