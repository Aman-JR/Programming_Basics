
# Difference is generic tree have  multiple child nodes
# Generic Tree

#          5
#    2   9   8   7
#      15  1
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTree(root):
    if root == None:
        return
    print(root.data)
    for i in root.children:
        printTree(i)

n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(9)
n4 = TreeNode(8)
n5 = TreeNode(7)
n6 = TreeNode(15)
n7 = TreeNode(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)

printTree(n1)