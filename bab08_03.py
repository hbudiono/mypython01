
# for line in open('test.txt') :
#     print(line,end='')


with open('test.txt') as myfile :
    for line in myfile:
        print(line,end='')

print('')

if myfile.closed :
    print('closed')
else:
    print('open')
