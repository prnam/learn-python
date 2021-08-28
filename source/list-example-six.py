# The group_list function accepts a group name and a list of members, and returns a string with the format:
# group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".
def group_list(group, users):
    members = "".join("{}: ".format(group)) + ", ".join(user for user in users)
    return members


# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print(group_list("Users", ""))  # Should be "Users:"
