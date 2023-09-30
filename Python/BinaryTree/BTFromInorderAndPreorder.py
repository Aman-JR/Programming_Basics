

import queue

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def takeInput():
    nodeData = int(input("Enter the Node data : "))
    if nodeData == -1:
        return None
    node = BinaryTreeNode(nodeData)
    q = queue.Queue()
    q.put(node)

    while (not(q.empty())):
        front = q.get()
        print("Enter the {0} right child data : ".format(front.data))
        leftData = int(input())
        if leftData != -1:
            leftChild = BinaryTreeNode(leftData)
            front.left = leftChild
            q.put(leftChild)
        print("ENter the {0} right child data : ".format(front.data))
        rightData = int(input())
        if rightData != -1:
            rightChild = BinaryTreeNode(rightData)
            front.right = rightChild
            q.put(rightChild)
    return node

def printBT(root):
    if root == None:
        return
    print("{0} : ".format(root.data),end = "")
    if root.left != None:
        print(root.left.data,end = ", ")
    if root.right != None:
        print(root.right.data)
    printBT(root.left)
    printBT(root.right)
    print()


root = takeInput()
printBT(root)



