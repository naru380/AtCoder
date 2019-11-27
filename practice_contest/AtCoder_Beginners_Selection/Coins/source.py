a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for ai in range(a+1):
    for bi in range(b+1):
        for ci in range(c+1):
            if (x-500*ai-100*bi-50*ci) == 0:
                count += 1

print(count)
