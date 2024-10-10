def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.value < max_val):
        return False
    return (is_bst(node.left, min_val, node.value) and
            is_bst(node.right, node.value, max_val))

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_level_order(arr, root, i, n):
    if i < n:
        if arr[i] is not None:
            temp = TreeNode(arr[i])
            root = temp
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    
    return root

def build_tree(arr):
    n = len(arr)
    return insert_level_order(arr, None, 0, n)

def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.value, end=" ")
        print_inorder(root.right)


arr = [10, 5, 15, None, None, 6, 20]
root = build_tree(arr)
if is_bst(root):
    print("True")
else:
    print("False")

