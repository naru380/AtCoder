n = int(input())
a = [int(i) for i in input().split(' ')]

a.sort()
it_a = iter(a)

alice = 0
bob = 0
for ai in it_a:
    alice += ai
    try:
        bob += next(it_a)
    except StopIteration:
        pass

print(abs(alice - bob))
