def countProperFractions(max_d):
    count = 0
    result = []
    for n in range(1, max_d):
        for d in range(1, max_d + 1):
            if n < d:
                if hcf(n, d) == 1:
                    result.append('{}/{}'.format(n, d))
                    count += 1
    print(result)
    return count


def hcf(n, d):
    while d:
        n, d = d, n % d
    return n


if __name__ == '__main__':
    max_d = int(input().strip())

    result = countProperFractions(max_d)

    print(result)
