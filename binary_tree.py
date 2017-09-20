class Tree:
    data = -1
    left_child = None
    right_child = None


def binary_tree_insert(node, y):
    if node is None:
        node = Tree()
        node.data = y
        node.left_child = node.right_child = None
    elif node.data == y:
        return node
    if y < node.data:
        node.left_child = binary_tree_insert(node.left_child, y)
    elif y > node.data:
        node.right_child = binary_tree_insert(node.right_child, y)
    return node


def binary_tree_build(values):
    tree = None
    for v in values:
        tree = binary_tree_insert(tree, v)
    return tree


def binary_tree_search(tree, key):
    if tree is None:
        return None
    if key == tree.data:
        return tree
    elif key < tree.data:
        return binary_tree_search(tree.left_child, key)
    else:
        return binary_tree_search(tree.right_child, key)


def binary_tree_delete_node(node):
    if node.left_child is None and node.right_child is None:
        del node
        return None
    elif node.left_child is None:
        temp = node.right_child
        node.data = node.right_child.data
        node.left_child = node.right_child.left_child
        node.right_child = node.right_child.right_child
        del temp
        return node
    elif node.right_child is None:
        temp = node.left_child
        node.data = node.left_child
        node.right_child = node.left_child.right_child
        node.left_child = node.left_child.left_child
        del temp
        return node
    else:
        temp = node
        right_root = node.left_child
        while right_root.right_child is not None:
            temp = right_root
            right_root = right_root.right_child
        if temp != node:
            temp.right_child = right_root.left_child
        else:
            temp.left_child = right_root.left_child
        node.data = right_root.data
        del right_root
        return node


def binary_tree_delete(tree, key):
    temp = tree
    if tree is None:
        return None
    else:
        if key == tree.data:
            temp = binary_tree_delete_node(tree)
        elif key < tree.data:
            tree.left_child = binary_tree_delete(tree.left_child, key)
        else:
            tree.right_child = binary_tree_delete(tree.right_child, key)
    return temp


def binary_tree_traverse_forhead(tree):
    print(tree.data)
    if tree.left_child is not None:
        binary_tree_traverse_forhead(tree.left_child)
    elif tree.right_child is not None:
        binary_tree_traverse_forhead(tree.right_child)


def binary_tree_traverse_middle(tree):
    if tree is not None:
        if tree.left_child is not None:
            binary_tree_traverse_middle(tree.left_child)
        print(tree.data)
        if tree.right_child is not None:
            binary_tree_traverse_middle(tree.right_child)


lists = [1, 67, 6, 89, 90]
binary_tree = binary_tree_build(lists)
# print(find_node.data)
binary_tree_traverse_forhead(binary_tree)
# binary_tree_traverse_middle(binary_tree)
# binary_tree = binary_tree_delete(binary_tree, 89)
# binary_tree_traverse_forhead(binary_tree)
