X = int(input())

u500 = X // 500
u5 = (X % 500) // 5

print(1000 * u500 + 5 * u5)
