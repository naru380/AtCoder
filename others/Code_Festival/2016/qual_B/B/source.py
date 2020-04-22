N, A, B = map(int, input().split())
S = input()

passed_japanese = 0
passed_foreigner = 0
ans = []

for i, c in enumerate(S):
    if A+B > passed_japanese+passed_foreigner:
        if c == 'a':
            passed_japanese += 1
            ans.append('Yes')
        elif c == 'b':
            if passed_foreigner+1 <= B:
                passed_foreigner += 1
                ans.append('Yes')
            else:
                ans.append('No')
        else:
            ans.append('No')
    else:
        ans.append('No')

print(*ans, sep="\n")
