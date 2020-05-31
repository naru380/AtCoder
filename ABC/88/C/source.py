# a1 を既知とすると
# c11 = a1 + b1 となり
# b1 = c11 - a1 が定まる
# さらに ci1 = ai + b1 であるから
# a2 = c21 - b1 と
# a3 = c31 - b1 が定まる
# すると b2 =  c12  - a1 と b3  = c13 - a1　も定まる
# よって (a1, a2, a3, b1, b2, b3) = (a1, c21-c11+a1, c31-c11+a1, c11-a1, c12-a1, c13-a1) と定まる
# ここで (a1, a2, a3, b1, b2, b3) = (p1+x, p2+x, p3+x, q1-x, q2-x, q3-x) とおけば
# x を適切に設定する事で a1 = 0 と仮定することができる (aiとbjでxが相殺される)
# 従って (a1, a2, a3, b1, b2, b3) = (0, c21-c11, c31-c11, c11, c12, c13) である

c = []
for _ in range(3):
	c.append(list(map(int,  input().split())))

a1, a2, a3, b1, b2, b3 = 0, c[1][0]-c[0][0], c[2][0]-c[0][0], c[0][0], c[0][1], c[0][2]

# print("(a1, a2, a3, b1, b2, b3) = ({}, {}, {}, {}, {}, {})".format(a1, a2, a3, b1, b2, b3))

if c[0][0] == a1 + b1 and c[0][1] == a1 + b2 and c[0][2] == a1 + b3 \
    and c[1][0] == a2 + b1 and c[1][1] == a2 + b2 and c[1][2] == a2 + b3 \
    and c[2][0] == a3 + b1 and c[2][1] == a3 + b2 and c[2][2] == a3 + b3:

    print("Yes")

else:

    print("No")
