def main():
    N, M, V, P = map(int, input().split())
    A = list(map(int, input().split()))
    sorted_A = sorted(A, reverse=True)

    def is_possible(i):
        # Aは降順 -> sorted_A、
        # i+1番目以降の問題のスコアをi番目の問題のスコア以下になるように投票すれば
        # i番目の問題に採用される可能性が生まれるという考え方

        # 投票前の上位P問は採用される可能性がある
        if i < P:
            return True

        # 残り投票数
        num_votes = V * M

        # i番目の問題を採用させようとする場合は、M人のジャッジ全員がi番目の問題に投票すればよい
        score_i = sorted_A[i] + M
        num_votes -= M

        # M人のジャッジ全員がi番目の問題に投票しても、上位P問にスコアが上がらない場合は採用される可能性がない
        if sorted_A[P - 1] > score_i:
            return False

        # 上の操作からi+1番目以降のの問題のスコアを、i番目の問題のスコアを超えることがないため、
        # M人のジャッジ全員がi+1番目以降の問題に投票してもよい
        num_votes -= (N - i - 1) * M

        # i番目の問題が上位P問に入ればよいので、P-1位の問題にもM人のジャッジ全員が投票してもよい
        num_votes -= (P - 1) * M

        # P番目からi番目
        # print('margin: {}, num_votes: {}'.format(sum(score_i - j for j in sorted_A[P-1 : i]), num_votes))
        return sum(score_i - j for j in sorted_A[P-1 : i]) >= num_votes

    # 1番目は必ず採用される
    # N番目は採用されるか
    if is_possible(N-1):
        print(N)

    # 1番目:採用、N番目:採用されない
    # -> [1:N-1]のどこに採用の境界があるかを二分探索する
    else:
        low = 0
        hight = N - 1

        while hight - low > 1:
            middle = (hight + low) // 2
            # print('PRE - low:{}, middle:{}, hight:{}'.format(low, middle, hight))
            if is_possible(middle):
                low = middle
            else:
                hight = middle
            # print('AFT - low:{}, middle:{}, hight:{}'.format(low, middle, hight))

        print(low + 1)


if __name__ == '__main__':
    main()
