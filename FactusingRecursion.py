def fact(n): 
    #if n is equals to 0 then factorial will be one!!
    if (n==0):   
    return 1        
    #If n == 3 then fact will be 6
    return n*fact(n-1) 
    
result = fact(6)

print(result)

