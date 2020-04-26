from collections import Counter

S = input()
MOD = 2019
mods = [0]
r = 0
for i, c in enumerate(S[::-1]):
    r += int(c) * pow(10, i, MOD)
    mods.append(r % MOD)

counter = Counter(mods)
# print("counter: {}".format(counter))

ans = 0
for v in counter.values():
    ans += v * (v-1) // 2

print(ans)
