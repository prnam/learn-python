arr = [1, -4, 7, 4, 2, -1, -7]
k = 0
count = 0
checked = {}
for item in arr:
    if k - item in arr and (k - item, item) not in checked.items():
        count += 1
        checked[item] = k - item
print(checked, count)