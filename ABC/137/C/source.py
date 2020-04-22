import itertools
from collections import Counter
import math

N = int(input())

def generate_prime_numbers():
    search_range = 150
    search_list = [True for i in range(0, search_range+1)]
    search_list[0] = False
    search_list[1] = False
    search_list[2] = True
    for i in range(2, search_range+1):
        for j in range(i*2, search_range+1, i):
            search_list[j] = False
    prime_numbers = [i for i in range(search_range+1) if search_list[i] == True]
    return prime_numbers[:27]

def combination(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

prime_numbers = generate_prime_numbers()
encoded_strings = []
for i in range(N):
    S = input()
    encoded_string = 1
    for c in S:
        char_to_int = ord(c) - ord('a')
        encoded_string *= prime_numbers[char_to_int]
    encoded_strings.append(encoded_string)
# print(encoded_strings)

ans = 0
# for comb in itertools.combinations(encoded_strings, 2):
#     if comb[0] == comb[1]:
#         ans += 1
counter = Counter(encoded_strings)
for i in counter.values():
    if i > 1:
        ans += combination(i, 2)

print(ans)
