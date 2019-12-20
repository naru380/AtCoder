import math

N = int(input())

for i in range(50001):
    price = math.floor(i * 1.08)
    if (N == price):
        print(i)
        exit(0)

print(':(')
