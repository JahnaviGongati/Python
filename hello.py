def fibonacci(n):
    if n<=0:
        return 'Invalid input'
    elif n==1 or n==2:
        return n-1
    else:
        a,b=0,1
        for i in range(n-2):
            a,b=b,a+b
        return b
n=int(input())
print(fibonacci(n))
