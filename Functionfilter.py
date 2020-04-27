# Here we are working on filter functions and it is a anonynomus function types
from functools import reduce # here we can also use "*"

cool_nums = [4,56,51,56,84,51,2,6,6,8,5625,6]

even = list(filter(lambda n: n%2==0, cool_nums))  

making2ble = list(map(lambda n: n*2, even))

sumsofcool_nums = (reduce(lambda a,b: a+b, cool_nums))

print ("These are some filtered even numbers",even)

print ("These are doubles of evens ",making2ble)

print(" Sums of list ",sumsofcool_nums)





# filter function is filtered evens 
[4, 56, 56, 84, 2, 6, 6, 8, 6]





