#formating
import math

print("First value : {1}, and second value : {0}".format(1+2,2))
print('First value : {1}, and second value : {0}'.format(5,2))

print("First value : {pertama}, and second value : {kedua}".format(pertama='Satu',kedua='Dua'))


#formating with space, decimal for integer and float

for i in range(1,11):
    print('{0:3.4f}{1:6d}{2:6d}'.format(i,i*i,i*i*i))

print("Formating pi:")
print("We can print pi as {0:.5f}".format(math.pi))