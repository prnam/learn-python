def efficientJanitor(weight):
    max_weight = 3.0
    trips = 0
    weight.sort()
    index, jump = 0, len(weight) - 1
    while index <= jump:
        trips += 1
        if weight[index] + weight[jump] <= max_weight:
            index += 1
        jump -= 1

    return trips


if __name__ == '__main__':
    weight_count = int(input().strip())
    weight = []

    for _ in range(weight_count):
        weight_item = float(input().strip())
        weight.append(weight_item)

    result = efficientJanitor(weight)

    print(result)