#procedure and function in python
#arguments (parameters)


print("======= Example 1 =======")

def myproc(para01):
    print(para01)
    print(para01)

myproc("test")

print("======= Example 2 =======")

def mul(a,b):
    return a*b

c=mul(10,2)
print(c)


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

