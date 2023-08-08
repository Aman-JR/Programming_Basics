
# Function to count the number of the pairs in the array
def PairSum(li,n,num):
    count = 0
    map = {}

    for i in range(n):
        if num - li[i] in map:
            count += map[num - li[i]]

        if li[i] in map:
            map[li[i]] += 1
        else:
            map[li[i]] = 1
    return count


# For array
n = int(input())
li = [(int(input())) for i in range(n)]
# Number to find the pair with
num = int(input())

ans = PairSum(li,n,num)
print(ans)