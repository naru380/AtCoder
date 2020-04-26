N = int(input())
a = [int(i) for i in input().split()]

rate_map = [0] * 9
for i in a:
    rate_map[8 if i // 400 > 8  else i // 400] += 1
base = len(list(filter(lambda x: bool(x), rate_map[:8])))
# print(rate_map)
print("{} {}".format(min(rate_map[8], 1) if not bool(base) else base, base+rate_map[8]))
