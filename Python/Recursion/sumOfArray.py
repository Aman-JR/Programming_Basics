# Sum of the array using the recursion

def recursion(li):
    if len(li) == 1:
        return li[0]
    return li[0] + recursion(li[1:])

print("Enter the element of the array separated using space : ")
li = [int(x) for x in input().split()]
ans = recursion(li)
print("Sum of the array is :",ans)
