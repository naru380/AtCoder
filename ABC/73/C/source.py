from collections import Counter

N = int(input())
memo = []
for _ in range(N):
  memo.append(int(input()))

counter = Counter(memo)

ans = 0
for k, v in counter.items():
  if v % 2 != 0:
    ans += 1

print(ans)
