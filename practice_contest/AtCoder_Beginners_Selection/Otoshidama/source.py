n, y =  [int(i) for i in input().split(' ')]

for i in range(n+1):
    for j in range(n-i+1):
        if y == 10000*i + 5000*j + 1000*(n-i-j):
            print('{} {} {}'.format(i, j, n-i-j))
            exit(0)

print('-1 -1 -1')
