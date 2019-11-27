n = int(input())
a = [int(i) for i in input().split(' ')]

count = -1
flag = True
while flag:
    for i in range(n):
        if a[i]%2 == 0:
            a[i] = a[i]/2
        else:
            flag = False
            break
    count += 1

print(count)
