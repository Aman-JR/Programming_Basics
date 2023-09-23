
#! Given an array check if the number is present in the array

def CheckIfNumInArray(li,x):
    if x == li[0]:
        return True
    if len(li) == 1 and li[0] != x:
        return False
    return CheckIfNumInArray(li[1:],x)

print("Enter the array elements : ")
li = list(map(int,input().split()))
x = int(input("Enter the number you want to search in the array : "))

ans = CheckIfNumInArray(li,x)
if ans == True:
    print("It's present in the given array")
else:
    print("It's not present in the array")



