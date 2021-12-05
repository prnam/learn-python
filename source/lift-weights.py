from itertools import combinations


def weightCapacity(weights, maxCapacity):
    max_value = 0
    for index in range(len(weights) + 1):
        list_combo = list(combinations(weights, index))
        print(list_combo)
        for item in list_combo:
            result = sum(item)
            if maxCapacity >= result > max_value:
                max_value = result
    return max_value


if __name__ == "__main__":
    size = int(input().strip())
    weights = []
    [weights.append(int(input().strip())) for index in range(size)]
    maxCapacity = int(input().strip())
    print(weightCapacity(weights, maxCapacity))
