def is_palindrome(string):
    return string == string[::-1]


def is_palindrome_without_using_slice(string):

    if not string:
        return False

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False

        right -= 1
        left += 1

    return True


if __name__ == "__main__":

    # print(is_palindrome("python"))
    # print(is_palindrome("madam"))
    print(is_palindrome_without_using_slice("python"))
    print(is_palindrome_without_using_slice("madam"))
