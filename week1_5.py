def fibonacci(n):
    if n<=0:
        return "Invaild input"
    elif n==1 or n==2:
        return n-1
    else:
        a,b=0,1
        for _ in range(n-2):
            a,b=b,a+b
        return b
n=int(input("enter the position (n) to find nth fibonacci number: "))
print(f"The {n}th fibonacci number is :",fibonacci(n))
