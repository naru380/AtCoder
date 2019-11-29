n, k = list(map(int, input().split()))
d = set(map(int, input().split()))

while(True):
    if(not({int(c) for c in str(n)} & d)):
        break
    n += 1

print(n)
