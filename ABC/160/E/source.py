X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

pX = sorted(p, reverse=True)[:X]
qY = sorted(q, reverse=True)[:Y]

D = pX + qY + r

print(sum(sorted(D, reverse=True)[:X+Y]))
