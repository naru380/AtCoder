ABCD = input()

for i in range(2**(len(ABCD)-1)):
    n = int(ABCD[0])
    ans = ABCD[0]
    for j, c in enumerate(format(i, '0' + str(len(ABCD)-1) + 'b')):
        if c == '0':
            n += int(ABCD[j+1])
            ans += '+'
        else:
            n -= int(ABCD[j+1])
            ans += '-'
        ans += ABCD[j+1]
    if n == 7:
        print(ans + '=7')
        exit(0)
