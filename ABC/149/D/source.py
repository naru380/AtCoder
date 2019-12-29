def main():
  N, K = map(int, input().split())
  R, S, P = map(int, input().split())
  T = input()

  set_rsp = set(['r', 's', 'p'])

  def vict_output(c):
    if c == 'r':
        output = 'p'
        point = P
    elif c == 's':
        output = 'r'
        point = R
    else:
        output = 's'
        point = S
    return output, point

  history = []
  score = 0
  for i in range(len(T)):
      # print('i: {}, T[i]: {}, pre_K_output: {}'.format(i, T[i], history[i-K:i-K+1]))
      # print('history: {}'.format(history))
      output, point = vict_output(T[i])
      if i >= K:
          # print('if1')
          pre_K_output = history[i - K]
          # K手前と等しかった場合
          if output == pre_K_output:
              # print('if2')
              point = 0
              # K手先に有利になるように見る
              if (i + K) <= (len(T) - 1):
                  # print('if3')
                  output, _ = vict_output(T[i + K])
                  if output == pre_K_output:
                        # print('if4')
                        # pre_K_input, _ = vict_output(pre_K_output)
                        # pre_K_input, _ = vict_output(pre_K_input)
                        # rest = list(set_rsp - set(pre_K_input))
                        # o1, p1 = vict_output(rest[0])
                        # o2, p2 = vict_output(rest[1])
                        o1, p1 = vict_output(pre_K_output)
                        o2, p2 = vict_output(o1)
                        # print('rest: {}'.format(rest))
                        # print('o1:{}, o2:{}'.format(o1, o2))
                        if (p1 > p2):
                            output = o1
                            # point = p1
                        else:
                            output = o2
                            # point = p2
                  else:
                        output, _ = vict_output(output)
                        output, _ = vict_output(output)
              else:
                  # この場合K手前の手以外ならなんでも良い
                  output, _ = vict_output(list(set_rsp - set(pre_K_output))[0])
                  # K手前以外のの手で最も得点が大きい手を選ぶ

      # print('output: {}, point: {}'.format(output, point))
      score += point
      history.append(output)

  # print(history)
  print(score)

if __name__ == '__main__':
    main()
