N, Y = list(map(int, input().split()))

for z in range(N+1):
    if 10000 * z > Y:
        break
    for y in range(N+1-z):
        if ((Y - (10000 * z + 5000 * y)) // 1000) == (N - (y + z)):
            print('{} {} {}' . format(z, y, N-y-z))
            exit(0)

print('-1 -1 -1')
