# Fib number using dynamic programming\


def fibNumber(n):
    if n == 0 or n == 1:
        return n
    elif memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fibNumber(n-1) + fibNumber(n-2)
        return memo[n]

def iterative_FibNumber(n):
    memo = [-1]*(n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        memo[i] = memo[i-1]+memo[i-2]
    return memo[n]

n = int(input("Enter the number whose fib number you want to find : "))
memo = [-1] * (n+1)
print(iterative_FibNumber(n))
