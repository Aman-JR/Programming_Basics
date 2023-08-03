
#! Binary Search in Python

def Binary_Search(li,k):
   start = 0
   end = len(li)-1

   while start <= end:
      # Find the mid element
      mid = start + (end - start)

      if li[mid] == k:
         # if found the element return the position
         return mid
      if li[mid] < k:
         start = mid + 1
      else:
         end = mid - 1
   # if element not present return -1
   return -1

#Creating list in python
n = int(input("Enter the size of the list in python : "))
li = [(int(input())) for i in range(0,n)]
print("List = ",li)

# Element to be searched in the list
k = int(input("ENter the element to be searched in the List : "))
ans = Binary_Search(li,k)
if ans == -1:
   print("Element not found")
else:
   print("Element found at position {0}".format(ans))
