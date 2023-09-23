

def powerOfNum(x,y):
    if y == 0:
        return 1
    return x * (powerOfNum(x,y-1))

x = int(input("Enter the number : "))
y = int(input("Enter the power : "))

ans = powerOfNum(x,y)
print("Power of number is :",ans)