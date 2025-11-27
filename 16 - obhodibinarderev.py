class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value   # значение в узле
        self.left = left     # левый ребёнок
        self.right = right   # правый ребёнок

def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")  # корень
    preorder(node.left)         # левое
    preorder(node.right)        # правое

def inorder(node):
    if node is None:
        return
    inorder(node.left)          # левое
    print(node.value, end=" ")  # корень
    inorder(node.right)         # правое

def postorder(node):
    if node is None:
        return
    postorder(node.left)        # левое
    postorder(node.right)       # правое
    print(node.value, end=" ")  # корень

# пример дерева:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = Node(1,
            Node(2, Node(4), Node(5)),
            Node(3))

print("Preorder:")
preorder(root)
print("\nInorder:")
inorder(root)
print("\nPostorder:")
postorder(root)
print()
