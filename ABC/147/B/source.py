S = input()

length = len(S)

ans = 0

for i in range(length//2):
    if S[i] != S[length - i - 1]:
        ans += 1

print(ans)
