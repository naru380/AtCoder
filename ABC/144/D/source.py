import math
import time

a, b, x = map(int, input().split())

theta = 0
if x/a > a*b/2:
    h = (a*b - x/a) * 2 / a
    theta = math.atan2(h, a)
else:
    w = x/a * 2 / b
    theta = math.atan2(b, w)
    
print(theta/math.pi*180)
