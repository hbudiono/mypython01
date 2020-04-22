# Control Flow
# for statement


mypets = ["cat","dog",'turtle']

print('====== contoh print list =========')

for a in mypets:
    print(a)


mystring = "Covid-19"

print('====== contoh pass =========')
for i in range(0,len(mystring)) :
    if i==3:  #stopper
      pass
    print(i,mystring[i])

print('====== contoh continue =========')
for i in range(0,len(mystring)) :
    if i==3:  #stopper
      continue
    print(i,mystring[i])
   
print('====== contoh break =========')
for i in range(0,len(mystring)) :
    if i==3:  #stopper
      break
    print(i,mystring[i])




