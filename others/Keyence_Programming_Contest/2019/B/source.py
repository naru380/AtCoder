S = input()
target = "keyence"
length = len(target)+1

# 部分文字列を取り除く方法は、
# 1. 先頭の文字列を削除
# 2. 真ん中の文字列を削除
# 3. 末尾の文字列を削除

if target in S: # 1 & 3
    print("YES")
    exit()
else: # 2
    for i in range(1, length):
      first = target[:i]
      second = target[i:]
      # print("{} + {}".format(S[0:len(first)], S[len(target)-len(second):len(target)]))
      if first in S and second in S and S.find(first) < S.rfind(second):
          if S[0:len(first)] + S[len(S)-len(second):len(S)] == target:
                print("YES")
                exit()
print("NO")
