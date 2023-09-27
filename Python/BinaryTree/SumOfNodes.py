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

def SumOfTheBT(root):
    if root == None:
        return 0
    leftSum = SumOfTheBT(root.left)
    print("Ls",leftSum)
    rightSum = SumOfTheBT(root.right)
    print("Rs",rightSum)
    return root.data + leftSum + rightSum

root = inputBT()
ans = SumOfTheBT(root)
print("Sum of the binary tree is : ",ans)


