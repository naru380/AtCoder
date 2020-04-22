from collections import Counter
from functools import reduce
N = int(input())
a = list(map(int, input().split()))

def print_yes():
    print('Yes')
    exit(0)

def print_no():
    print('No')
    exit(0)

if not any(a):
    print('Yes')
else:
    if N % 3 == 0:
        counter = Counter(a)
        # print(counter)
        if len(counter) == 3:
            for i in counter.values():
                if i != N / 3:
                    print_no()
            if reduce(lambda a,b: a^b, list(counter.keys())) == 0:
                print_yes()
            else:
                print_no()
        elif len(counter) == 2:
            if a.count(0) == N/3:
                print_yes()
            else:
                print_no()
        else:
            print_no()
    else:
        print_no()
