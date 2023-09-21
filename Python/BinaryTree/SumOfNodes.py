class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inputBT():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = inputBT()
    rightTree = inputBT()
    root.left = leftTree
    root.right = rightTree

    return root