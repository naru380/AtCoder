from collections import deque

K = int(input())

queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

x = 1
count = 0
while K != count:
    x = queue.popleft()
    if (x % 10) != 0:
        queue.append(10 * x + (x % 10) - 1)
    queue.append(10 * x + (x % 10))
    if (x % 10) != 9:
        queue.append(10 * x + (x % 10) + 1)
    count += 1
print(x)
