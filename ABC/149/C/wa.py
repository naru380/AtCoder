# この実装だと、以下のような「カーマイケル数」が素数であると誤判定される
# 561, 1105, 1729, 2465, 2821, 6601, 8911, …
def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

def main():
  X = int(input())

  n = X
  while not is_prime(n):
      n += 1

  print(n)

if __name__ == '__main__':
    main()
