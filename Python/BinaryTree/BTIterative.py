#! Binary Tree using iteration

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def  takeInput():
    nodeData = int(input())
    if nodeData == -1:
        return None
    root = BinaryTreeNode(nodeData)
    