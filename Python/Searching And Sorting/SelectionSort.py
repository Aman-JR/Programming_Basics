
# Selection sort is the algo which selects the smallest element from an unsorted list in each iteration and places that
# element at the beginning of the unsorted list.

def selectionSort(arr,n):
    for i in range(0,n-1):
        check = i
        for j in range(i+1,n):
            if arr[j] < arr[check]:
                check = j
        arr[i],arr[check] = arr[check],arr[i]
    pass


li = [int(ele) for ele in input().split()]
print("Before the sorting list is")
print(li)
selectionSort(li,len(li))
print("After the sorting the list is")
print(li)
