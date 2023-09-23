
#! Find the first index of the element in the given array

def findFirstIndex(li,x,count):
    if li[0] == x:
        return count
    if li[0] != x and len(li) == 1:
        return -1
    return findFirstIndex(li[1:],x,count+1)

print("Enter the array elements : ")
li = [int(x) for x in input().split()]
c = int(input("Enter the number to be checked in the array : "))
count = 0
ans = findFirstIndex(li,c,count)
if ans == -1:
    print("Not Present")
else:
    print("Present at ",ans)

