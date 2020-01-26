import math

# エラストテネスの篩
def eratosthenes(limit):
    A = [i for i in range(2, limit+1)]
    P = []
    time = 0

    while True:
        prime = min(A)

        if prime > math.sqrt(limit):
            break

        P.append(prime)

        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1

    for a in A:
        P.append(a)

    return P

def main():
  X = int(input())

  # ルジャンドル予想(未証明だが、、)
  # -> n^2 と (n+1)^2 の間に必ず素数が存在する
  # 10^(5/2) = 316.2277...
  # 317^2 = 100489
  P = eratosthenes(10**5+489)

  i = 0
  while True:
      if P[i] >= X:
          break
      i += 1

  print(P[i])

if __name__ == '__main__':
    main()
