
#! Create a BT using pre and in order
# # Steps to follow:
# 1. Find the root
# 2. Find in-order of both the left and the right sub Tree
# 3. Find pre order of the right and the left subtree
# 4. use recursion to build the left and the right subtree
# 5. create the left and right with the help of root and return the root



class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def BTfromIOandPo(io,po):
    if len(po) == 0:
        return None

    rootData = po[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInOrder = -1
    for i in range(0, len(io)):
        if io[i] == rootData:
            rootIndexInInOrder = i
            break
    if rootIndexInInOrder == -1:
        return None
    leftInorder = io[0:rootIndexInInOrder]
    rightInorder =io[rootIndexInInOrder+1:]

    lenLeftSubTree = len(leftInorder)

    leftPreorder = po[1+lenLeftSubTree+1]
    rightPreorder = po[lenLeftSubTree+1:]

    leftChild = BTfromIOandPo(leftPreorder,leftInorder)
    rightChild = BTfromIOandPo(rightPreorder,rightInorder)
    root.left = leftChild
    root.right = rightChild
    return root



print("Enter the In-order : ")
io = [int(i) for i in input().split()]

print("Enter the Pre-order : ")
po = [int(i) for i in input().split()]






def buildTreeHelper(preOrder,preStart, preEnd,inOrder,inStart,inEnd):
    if (preStart > preEnd) or (inStart > inEnd):
        return None

    rootData = preOrder[preStart]
    root = BinaryTreeNode(rootData)

    l = 0
    for i in range(inStart, inEnd+1):
        if rootData == inOrder[i]:
            l = i
            break
    root.left = buildTreeHelper(preOrder, preStart+1, preStart + (l-inStart), inOrder, inStart, l-1)
    root.right = buildTreeHelper(preOrder, preStart + (l - inStart)+1, preEnd,inOrder,l+1,inEnd)
    return root

def buildTree(preOrder,inOrder, n):
    preStart = 0
    preEnd = n-1
    inStart = 0
    inEnd = n-1
    return buildTreeHelper(preOrder,preStart,preEnd,inOrder, inStart, inEnd)
