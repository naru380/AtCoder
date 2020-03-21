# 間違えて作った上下左右に移動できる場合の解答

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.extend(input())
    # print(S)
# print(len(S))

T = [0] * H * W

k = 0

if S[k] == '#':
    T[k] = 1
else:
    T[k] = 0

U = [False] * H * W
U[k] = True

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
    next_x = x-1
    next_y = y-1
    if 0 <= next_x:
        p.append(W*y+next_x)
    if 0 <= next_y:
        p.append(W*next_y+x)
    return p

while True:
    # print('k:{}'.format(k))
    # print('R:{}'.format(R))
    p = get_search_address(k)
    # print('p:{}'.format(p))
    for n in p:
        # print('n:{}'.format(n))
        if S[n] == '#':
            # print('#')
            if not U[n]:
                # print('test1')
                T[n] = T[k]+1
                R[n] = T[n]
                U[n] = True
            else:
                # print('test2')
                if T[n] > T[k]+1:
                    # print('test3')
                    T[n] = T[k]+1
                    R[n] = T[n]
        else:
            # print('.')
            if not U[n]:
                # print('test4')
                T[n] = T[k]
                R[n] = T[n]
                U[n] = True
            else:
                # print('test5')
                if T[n] > T[k]:
                    # print('test6')
                    T[n] = T[k]
                    R[n] = T[n]

    # print('T:{}'.format(T))
    del R[k]
    if not R:
        break
    k = min(R, key=R.get)

print(T[H*W-1])
