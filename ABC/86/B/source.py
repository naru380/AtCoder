a, b = input().split()
ab = int(a+b)

for i in range(1, 100100):
  if i**2 == ab:
    print("Yes")
    exit(0)
print("No")
