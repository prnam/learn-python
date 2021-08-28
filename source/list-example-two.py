# Complete the skip_elements function to return every other element from the list,
# using the enumerate function to check if an element is on an even position or an odd position.
def skip_elements(elements):
    # code goes here
    new_list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_list.append(element)
    return new_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"]))
