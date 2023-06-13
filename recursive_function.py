

# Iterative function

def find_sum(n):
    sum = 0
    for i in range(n+1):
        print(i, sum)
        sum += i
    
    return sum

print(find_sum(5))


# Recursive function

def rfind_sum(n):
    if n==1:
        return 1
    return n + rfind_sum(n-1)

print(rfind_sum(5))

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))