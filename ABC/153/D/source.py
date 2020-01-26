import math

H = int(input())

count = 1
while True:
    if H == 1:
        break
    H = math.floor(H/2)
    count += 1

print(2**count-1)
