def adder(*num):
    sum = 0    
    for n in num:
        sum = sum + n
    print("Sum:", sum)
adder(3,2)
adder(2,5,6,8)
adder(5,2,5,8)

Sum: 5
Sum: 21
Sum: 20

