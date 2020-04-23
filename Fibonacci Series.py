#Printing Fibonacci Numbers 

print("Fibonacci Numbers")
n = int(input("Enter a number"))
def fib(n):  
  a = 0
  b = 1
  print(a)
  print(b)
  
  if n < 0:
    print("Number can't be taken below zero!!") 
  else:
        for i in range(2 , n): # for i in range(2 , 12): if we want to print till specific index 
        c = a+b
        a = b 
        b = c
        print c
fib(n)        
     
      
