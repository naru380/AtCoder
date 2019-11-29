w = input()
freq = {}

for c in w:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

if len(list(filter(lambda x: x%2==0, freq.values()))) == len(freq.keys()):
    print('Yes')
else:
    print('No')
