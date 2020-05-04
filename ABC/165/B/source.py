X = int(input())

money = 100
count = 0
while money < X:
    count += 1
    money = (money * 1.01) // 1

print(count)
