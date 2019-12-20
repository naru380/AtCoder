def main():
    change = 1000 - int(input())

    coins = [500, 100, 50, 10, 5, 1]

    ans = 0
    for coin in coins:
        while change >= coin:
            # print(change)
            change -= coin
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
