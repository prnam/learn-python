def getSumOfDoubleBasePalindrome(maximum):
    result = 0
    for number in range(1, maximum + 1):
        output = isPalindrome(number)
        result += output
    return result


def isPalindrome(number: int):
    """
    Checks for palindrome for given number for base 10 and 2
    :param number:
    :return:
    """
    reverse = 0
    borrow_number = number
    while borrow_number > 0:
        reverse = reverse * 10 + borrow_number % 10
        borrow_number = borrow_number // 10

    if number == reverse:
        binary = "{0:b}".format(number)
        if binary[::-1] == binary:
            return number
        else:
            return 0
    else:
        return 0


if __name__ == "__main__":
    maximum = int(input().strip())

    result = getSumOfDoubleBasePalindrome(maximum)

    print(result)
