class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def printBT(root):
    if root == None:
      return
    print(root.data,end = " : ")
    if root.left != None:
        print("L",root.left.data)
    if root.right != None:
        print("R",root.right.data)
    print()
    printBT(root.left)
    printBT(root.right)


def treeInputRecursion():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInputRecursion()
    rightTree = treeInputRecursion()
    root.left = leftTree
    root.right = rightTree
    return root

root = treeInputRecursion()
printBT(root)

