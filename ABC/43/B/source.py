s = input()
ans = []
for c in s:
    if (c == 'B'):
        if (len(ans) > 0):
            ans.pop(-1)
    else:
        ans.append(c)

print(''.join(ans))
