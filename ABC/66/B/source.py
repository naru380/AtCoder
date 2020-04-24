S = input()

def is_even_string(string):
    # print("str1: {}, str2: {}".format(string[:len(string)//2], string[len(string)//2:]))
    if string[:len(string)//2] == string[len(string)//2:]:
        return True
    else:
        return False

for i in range(2, len(S), 2):
    new_S = S[:len(S)-i]
    # print("new_S: {}".format(new_S))
    if is_even_string(new_S):
        print(len(new_S))
        exit(0)
