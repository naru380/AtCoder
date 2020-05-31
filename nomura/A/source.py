H1, M1, H2, M2, K = map(int, input().split())

time = (60*H2+M2) - (60*H1+M1)

print(max(time-K, 0))
