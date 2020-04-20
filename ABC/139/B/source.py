A, B = map(int, input().split())

count = 1
ans = 0

while count < B:
    count += A - 1
    ans += 1

print(ans)
