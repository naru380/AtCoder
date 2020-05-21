from collections import Counter

DEBUG = False

N = int(input())
S = []
patterns = []
ans = 0
for _ in range(N):
    s = input()
    # S.append(s)
    ans += s.count("AB")
    # 3進数表記 -> 1bit目: 先頭の文字, 2bit目: 末尾の文字
    # A = 0, B = 1, O:other = 2
    # A...A: 0, A...B: 1, A...O: 2
    # B...A: 3, B...B: 4, B...O: 5
    # O...A: 6, O...B: 7, O...O: 8
    pattern = ""
    pattern += "2" if (s[0] != "A"  and s[0] != "B") else "1" if s[0] == "B" else "0"
    pattern += "2" if (s[-1] != "A" and s[-1] != "B") else "1" if s[-1] == "B" else "0"
    patterns.append(int(pattern, 3))
    if DEBUG:
        print("s: {}, pattern: {}".format(s, pattern))

if DEBUG:
    print("patterns: {}".format(patterns))
    print("ans: {}".format(ans))

counter = Counter(patterns)
if DEBUG:
    print("counter: {}".format(counter))

ans += counter[3] - 1 if counter[3] else 0
if DEBUG:
    print("ans: {}".format(ans))


num_tail_A = counter[0] + counter[6]
num_head_B = counter[4] + counter[5]
if DEBUG:
    print("num_tail_A: {}, num_head_B: {}".format(num_tail_A, num_head_B))

if not num_tail_A and not num_head_B:
    pass
else:
    num_tail_A += 1 if counter[3] else 0
    num_head_B += 1 if counter[3] else 0
    ans += min(num_tail_A, num_head_B)

print(ans)
