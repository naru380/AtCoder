S = input()

length = len(S)
is_strong_palindrome = True

for i in range(length//2):
    if S[i] != S[length-i-1]:
        is_strong_palindrome = False
        break

first_half_S = S[:length//2]
second_half_S = S[length//2+1:]
# print(first_half_S)
# print(second_half_S)

length_palindrome = len(first_half_S)
for i in range(length_palindrome//2):
    if first_half_S[i] != first_half_S[length_palindrome-i-1]:
        is_strong_palindrome = False
        break
    if second_half_S[i] != second_half_S[length_palindrome-i-1]:
        is_strong_palindrome = False
        break

if is_strong_palindrome:
    print("Yes")
else:
    print("No")
