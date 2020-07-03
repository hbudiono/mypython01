#another example of exception

def divide(x,y):
    try:
       result = x / y
    except ZeroDivisionError :
       print('Pembagian dengan nol')
    return result


print(divide(10,2))