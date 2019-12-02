'''
$B!V%"%s%P%i%s%9(B = $BItJ,J8;zNs$K=P8=$9$kJ8;z$NCf$G!"B>$N$I$NJ8;z$h$jB?$/=P8=$9$kJ8;z$,B8:_!W$H8mG'(B
 ex) $B!V(Babca$B!W(B $B$O!"(Ba:2, b:1, c:1 $B$J$N$G%"%s%P%i%s%9(B -> $B4V0c$$!JJ8;zNsD9(B4$B$KB-$7$F(Ba:2$B$J$N$G2aH>?t$K$J$C$F$$$J$$!K(B
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
