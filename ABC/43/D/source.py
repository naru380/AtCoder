s = input()

if len(s) == 2:
    if s[0] == s[1]:
        print('1 2')
    else:
        print('-1 -1')
else:
    for i in range(2, len(s)):
        if s[i-1] == s[i]:
            print('{} {}' . format(i, i+1))
            exit(0)
        elif s[i-2] == s[i]:
            print('{} {}' . format(i-1, i+1))
            exit(0)
    print('-1 -1')
