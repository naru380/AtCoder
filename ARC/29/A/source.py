N = int(input())
T = [int(input()) for _ in range(N)]

ans = sum(T)
for i in range(2**N):
    bin_i = format(i, '0' + str(N)  + 'b')
    machine1 = 0
    machine2 = 0
    for n, c in enumerate(bin_i[::-1]):
        if c == '1':
            machine1 += T[n]
        else:
            machine2 += T[n]
    if abs(machine1 - machine2) < ans:
        ans = abs(machine1 - machine2)

ans = (sum(T) - ans) // 2 + ans

print(ans)

