class binaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = binaryTreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def printBT(root):
    if root == None:
        return
    print(root.data,end = " : ")
    if root.left != None:
        print("L",root.left.data,end = ", ")
    if root.right != None:
        print("R",root.right.data, end = ", ")
    print()
    printBT(root.left)
    printBT(root.right)


def NodesGreater(root,x):
    if root == None:
        return
    NodesGreater(root.left,x)
    NodesGreater(root.right,x)
    if root.data > x:
        return 1
    pass


root = takeInput()
printBT(root)



