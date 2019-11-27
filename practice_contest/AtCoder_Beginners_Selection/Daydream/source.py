s = input()

i = 0
while len(s) > i:
    word = s[i:i+5]
    if(word == 'dream'):
        i += 5
        if(s[i:i+3] == 'era'):
            pass
        elif(s[i:i+2] == 'er'):
            i += 2
    elif(word == 'erase'):
        i += 5
        if(s[i:i+1] == 'r'):
            i += 1
    else:
        break

if(len(s) == i):
    print('YES')
else:
    print('NO')
