N = int(input())

for i in range(int(N**0.5)+1, 0, -1):
    div, mod = divmod(N, i)
    if not mod:
        print(len(str(max(div, N//div))))
        exit()
