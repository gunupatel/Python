from array import *
# vals = array('i',[5,9,-8,4])
# # print(vals.buffer_info())
#
# for i in range(4):
#     print(vals[i])

# take input from user

arr=array('i',[])
n=int(input("Enter the length of array"))
for i in range(n):
    x =int(input("Enter the value of array"))
    arr.append(x)

print(arr)

val=int(input('enter the value to serach'))
print(arr.index(val))
