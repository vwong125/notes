class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def inorder(node):
        if (node):
            TreeNode.inorder(node.left)
            print(node.val, end=" ")
            TreeNode.inorder(node.right)

    @staticmethod
    def preorder(node):
        if (node):
            print(node.val, end=" ")
            TreeNode.inorder(node.left)
            TreeNode.inorder(node.right)

    @staticmethod
    def postorder(node):
        if (node):
            TreeNode.inorder(node.left)
            TreeNode.inorder(node.right)
            print(node.val, end=" ")


def main():
    test_tree = TreeNode(1, TreeNode(2), TreeNode(3))
    TreeNode.inorder(test_tree)
    TreeNode.preorder(test_tree)
    TreeNode.postorder(test_tree)

if __name__ == '__main__':
    main()
    