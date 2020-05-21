sx, sy, tx, ty = map(int, input().split())
dist_x, dist_y = abs(tx-sx), abs(ty-sy)

# print("dist_x: {}, dist_y: {}".format(dist_x, dist_y))

path1 = ""
path2 = ""
path3 = ""
path4 = ""

if dist_x == 0 and dist_y == 0:
    pass
elif dist_x == 0 and dist_y != 0:
    path1 += "D"*disy_y if sy > ty else "U"*dist_y
    path2 += "U"*disy_y if sy > ty else "D"*dist_y
    path3 += "D"*disy_y if sy > ty else "U"*dist_y
    path4 += "U"*disy_y if sy > ty else "D"*dist_y
elif dist_x != 0 and dist_y == 0:
    path1 += "L"+dist_x if sx > tx else "R"*dist_x
    path2 += "R"+dist_x if sx > tx else "L"*dist_x
    path3 += "L"+dist_x if sx > tx else "R"*dist_x
    path4 += "R"+dist_x if sx > tx else "L"*dist_x
else:
    path1 += "D"*disy_y if sy > ty else "U"*dist_y
    path1 += "L"+dist_x if sx > tx else "R"*dist_x

    path2 += "U"*disy_y if sy > ty else "D"*dist_y
    path2 += "R"+dist_x if sx > tx else "L"*dist_x

    path3 += "R" if sx > tx else "L"
    path3 += "D"*(disy_y+1) if sy > ty else "U"*(dist_y+1)
    path3 += "L"*(disy_x+1) if sx > tx else "R"*(dist_x+1)
    path3 += "U" if sy > ty else "D"

    path4 += "L" if sx > tx else "R"
    path4 += "U"*(disy_y+1) if sy > ty else "D"*(dist_y+1)
    path4 += "R"*(disy_x+1) if sx > tx else "L"*(dist_x+1)
    path4 += "D" if sy > ty else "U"

print(path1+path2+path3+path4)
