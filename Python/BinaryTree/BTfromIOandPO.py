
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
    pass
    

print("Enter the In-order : ")
io = [int(i) for i in input().split()]

print("Enter the Pre-order : ")




