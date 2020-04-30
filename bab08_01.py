#exceptions

while True : 
    try:
      x=int(input('input an integer: '))
      break
    except Warning:
        print('This is a warning')
    except ValueError:
        print('This is a value error')