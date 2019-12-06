D, G = list(map(int, input().split()))
pc = [list(map(int, input().split())) for _ in range(D)]

ans = sum([i[0] for i in pc])

for i in range(2**D):
    search_index = format(i, '0' + str(D) + 'b')
    complete_answered = [i for i, c in enumerate(search_index[::-1]) if c == '1']
    incomplete_answered = list(set(range(D)) - set(complete_answered))
    answered_number = 0
    remaining_score = G
    for j in complete_answered:
        answered_number += pc[j][0]
        remaining_score -= (100 * (j + 1) * pc[j][0] + pc[j][1])
    incomplete_answered = sorted(incomplete_answered, reverse=True)
    for j in incomplete_answered:
        question_number = pc[j][0]
        while remaining_score > 0:
            answered_number += 1
            remaining_score -= 100 * (j + 1)
            question_number -= 1
            if question_number <= 0:
                remaining_score -= pc[j][1]
                break
    if answered_number < ans:
       ans = answered_number
print(ans)
