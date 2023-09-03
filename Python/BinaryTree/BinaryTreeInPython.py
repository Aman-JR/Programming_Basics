class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def printBT(root):
    if root == None:
      return
    print(root.data)
    if root.left != None:
        printBT(root.left)
    printBT(root.right)
    pass