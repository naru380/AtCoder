A, B, C = map(int, input().split())

count = 1
while B > count:
  if A * count % B == C:
    print("YES")
    exit(0)
  count += 1
print("NO")
