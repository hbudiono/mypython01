#file operation

f=open('my file.txt','a')
f.write('This is a test to write to this file\n')

f.close()

f=open('my file.txt','r')

for line in f:
    print(line,end='')

f.close()