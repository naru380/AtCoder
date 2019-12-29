def main():
  A, B, K = map(int, input().split())

  if K - A <= 0:
      print('{} {}'.format(A-K, B))
  else:
      if (B - (K - A)) >= 0:
          print('{} {}'.format(0, (B - (K - A))))
      else:
          print('{} {}'.format(0, 0))

if __name__ == '__main__':
    main()
