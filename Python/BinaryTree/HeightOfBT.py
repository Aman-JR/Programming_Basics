class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def heightOfBT(root):
    if root == None:
        return 0
    leftHeight = heightOfBT(root.left)
    rightHeight = heightOfBT(root.right)
    print(leftHeight,rightHeight)
    return 1 + max(leftHeight,rightHeight)


root = takeInput()
ans = heightOfBT(root)
print("Height of the binary tree is : ",ans)
