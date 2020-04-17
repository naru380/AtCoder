S = input()

ans = [0] * (len(S)+1)

for i in range(len(S)):
    if S[i] == "<":
        ans[i+1] = ans[i]+1
# print(ans)

for i in range(len(S)):
    if S[len(S)-i-1] == ">":
        ans[len(S)-i-1] = max(ans[len(S)-i-1], ans[len(S)-i]+1)
# print(ans)

print(sum(ans))
