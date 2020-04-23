#function in python

#Fibonacci series

print("===== Fibonnaci as a procedure ========")

def fib(n):
    a,b=0,1
    while a<n :
        print(a,end=' ')
        a,b=b,a+b
    print()

fib(1000)

print("===== Fibonnaci as a function ========")

def ffib(n):
    result = []
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

print(ffib(1000))

