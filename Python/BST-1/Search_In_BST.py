# Search in BST

import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def searchInBST(root, ele):
    pass

def takeInput():
    q = queue.Queue()
    rootData = int(input("Enter the root Data : "))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        front = q.get()
        print("Enter the left child of {0}".format(front.data))
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            front.left = leftChild
            q.put(leftChild)
        print("Enter the right child of {0}".format(front.data))
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            front.right = rightChild
            q.put(rightChild)
    return root
# def TakeInput():
#     q = queue.Queue()
#     rootData = int(input("Enter the root data : "))
#     if rootData == -1:
#         return None
#     root = BinaryTree(rootData)
#     q.put(root)
#     while (not(q.empty())):
#         front = q.get()

#         print("Enter the {0} left child".format(front.data))
#         rootLeftChild = int(input())
#         if rootLeftChild != -1:
#             leftChild = BinaryTree(rootLeftChild)
#             front.left = leftChild
#             q.put(leftChild)

#         print("Enter the {0} right child : ".format(front.data))
#         rootRightChild = int(input())
#         if rootRightChild != -1:
#             rightChild = BinaryTree(rootRightChild)
#             front.right = rightChild
#             q.put(rightChild)
#     return root

def printBT(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data, end = " ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


root = takeInput()
printBT(root)

