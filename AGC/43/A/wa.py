H, W = map(int, input().split())
S = []
for _ in range(H):
    S.extend(input())
    # print(S)
print(len(S))

T = [-1] * H * W
if S[0] == '#':
    T[0] = 1
else:
    T[0] = 0
S[0] = '-'

k = 0
v = T[k]
R = {k:v}

def get_search_address(add):
    p = []
    x = add % W
    y = add // W
    next_x = x+1
    next_y = y+1
    if next_x <= (W-1):
        p.append(W*y+next_x)
    if next_y <= (H-1):
        p.append(W*next_y+x)
    return p

while R:
    k = min(R, key=R.get)
    print('k:{}'.format(k))
    p = get_search_address(k)
    print('p:{}'.format(p))
    for n in p:
        print('n:{}'.format(n))
        if T[n] == -1:
            if S[n] == '-':
                if T[k]+1 < T[n]:
                    T[n] = T[k]+1
            elif S[n] == '#':
                T[n] = T[k]+1
                S[n] = '-'
                R[n] = T[n]
            else:
                T[n] = T[k]
                S[n] = '-'
                R[n] = T[n]
    del R[k]
    print('R:{}'.format(R))
    print('T:{}'.format(T))

print(T[H*W-1])
