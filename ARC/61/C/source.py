import math

S = input()

ans = 0
for i in range(2**(len(S)-1)):
    j = 0
    k = 1
    for c in format(i, '0' + str(len(S)-1) + 'b'):
        if c == '1':
            ans += int(S[j:k])
            j = k
        k += 1
    ans += int(S[j:k])

print(ans)
