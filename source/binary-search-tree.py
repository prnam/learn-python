class BSTreeNode:
    def __init__(self, node_value) -> None:
        self.value = node_value
        self.left = self.right = None


def isPresent(root, val):
    if root is None:
        return 0
    if root.value == val:
        return 1
    elif root.value > val:
        return isPresent(root.left, val)
    else:
        return isPresent(root.right, val)


def insert(root, val):
    if root is None:
        root = BSTreeNode(val)
        return root
    if val < root.value:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


if __name__ == "__main__":
    tree_size = int(input().strip())
    for index in range(tree_size):
        if index == 0:
            root = insert(None, int(input().strip()))
        else:
            insert(root, int(input().strip()))

    val = []
    val_size = int(input().strip())
    for _ in range(val_size):
        val.append(int(input().strip()))

    for value in val:
        print(isPresent(root, value))
