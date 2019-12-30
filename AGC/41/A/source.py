def main():
    N, A, B = map(int, input().split())
    result = N
    if (A % 2 == 0 and B % 2 == 0) or  (A % 2 == 1 and B % 2 == 1):
        result = abs(A - B) // 2
    else:
        if A - 1 < N - B:
            result = ((B - 1) - (A - 1 + 1)) // 2 + (A - 1 + 1)
        else:
            result = ((N - A) - (N - B + 1)) // 2 + (N - B + 1)

    print(int(result))

if __name__ == '__main__':
    main()
