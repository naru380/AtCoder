N = int(input())

if N % 2 == 1:
    ans = 0
else:
    count = 1
    ans = 0
    while N//2 >= 5**count:
        ans += N//(2*5**count)
        count+=1

print(ans)
