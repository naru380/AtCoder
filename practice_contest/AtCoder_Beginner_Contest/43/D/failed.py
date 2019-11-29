'''
「アンバランス = 部分文字列に出現する文字の中で、他のどの文字より多く出現する文字が存在」と誤認
 ex) 「abca」 は、a:2, b:1, c:1 なのでアンバランス -> 間違い（文字列長4に足してa:2なので過半数になっていない）
'''

s = input()
ds = {}
for c in s:
    if not(c in ds):
        ds[c] = 1
    else:
        ds[c] += 1

if len(s) == len(ds):
    print('-1 -1')
else:
    sorted_ds = sorted(ds.items(), key=lambda x:x[1], reverse=True)
    most_freq = max(sorted_ds, key=lambda y: y[1])[1]
    filtered_ds = dict(filter(lambda x: x[1]==most_freq, sorted_ds))
    a = b = 0
    flag = False
    for n, c in enumerate(s):
        if c in filtered_ds:
            filtered_ds[c] -= 1
            if len(list(filter(lambda x: x==most_freq, filtered_ds.values()))) == 0 and not(flag):
                a = n+1
                flag = True
            if len(list(filter(lambda x: x==0, filtered_ds.values()))) == len(filtered_ds):
                b = n+1
                flag = False
    print('{} {}'.format(a, b))
