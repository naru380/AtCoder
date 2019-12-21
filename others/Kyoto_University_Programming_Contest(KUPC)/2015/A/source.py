N = int(input())
S = [input() for _ in range(N)]
# print(S)

for s in S:
    tape = s
    index_tokyo = tape.find('tokyo')
    index_kyoto = tape.find('kyoto')
    # print(tape)
    # print('{} {}'.format(index_tokyo, index_kyoto))
    ans = 0
    while index_tokyo != -1 or index_kyoto != -1:
        # print(tape)
        if index_tokyo == -1:
            tape = tape[index_kyoto+5:]
        elif index_kyoto == -1:
            tape = tape[index_tokyo+5:]
        else:
            tape = tape[index_tokyo+5:] if index_kyoto > index_tokyo else tape[index_kyoto+5:]
        index_tokyo = tape.find('tokyo')
        index_kyoto = tape.find('kyoto')
        ans += 1
    print(ans)
