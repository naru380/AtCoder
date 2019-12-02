X = input()

Xzero = X.zfill(len(X)+3)
Xzero = Xzero[::-1]

simo = Xzero[0:2]
simo = int(simo[::-1])
kami = Xzero[2:len(Xzero)]
kami = int(kami[::-1])

n = 0
for i in range(20):
    if(simo <= i*5):
        break
    n += 1

if (kami >= n):
    print('1')
else:
    print('0')
