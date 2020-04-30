

while True : 
    try:
      x=int(input('input an integer: '))
      break
    except ValueError:
        print('Oops it is wrong data type, try it again')