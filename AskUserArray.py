from array import *
arr = array('i',[])

n = int(input("Enter the length or array"))

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)

# Here we are using for loop to find an index of an arr element
val = int(input("Enter the value for search"))

k = 0
for e in arr:
    if e==val:
        print(k,"Searched Element")
        break
    k+=1
else:
    print (val,'Desired value not found')

arr.reverse() # Here we are reversing the array
print(arr,"Array reversed")