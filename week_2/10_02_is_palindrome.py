input = "abcba"
# 소주만병만주소
# 주만병만주
# 만병만


def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1])

print(is_palindrome(input))