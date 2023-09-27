
#! PRINT BINARY TREE LEVEL WISE

import queue

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    q = queue.Queue()
    rootData = int(input("Enter the root data : "))
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    q.put(root)

    while (not(q.empty())):
        front = q.get()

        leftChildData = int(input("Enter the left child data of {0} : ".format(front.data)))
        if leftChildData  != -1:
            leftChild = BinaryTreeNode(leftChildData)
            front.left = leftChild
            q.put(leftChild)
        rightChildData = int(input("Enter the Right child data of {0} : ".format(front.data)))
        if rightChildData  != -1:
            rightChild = BinaryTreeNode(rightChildData)
            front.left = rightChild
            q.put(rightChild)
    return root

def printBT(root):
    if root == None:
        return
    q = []
    while len(q) > 0:
        print (q[0].data, end = " : ")
        node = queue.pop(0)
        if node.left is not None:
            print("L",node.left.data,end = ", ")
            queue.append(node.left)
        if node.right is not None:
            print("R",node.right.data)
            queue.append(node.right)


root = takeInput()
printBT(root)