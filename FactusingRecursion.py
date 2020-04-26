def fact(n): 
    if (n==0):   
    return 1        # n's value is 1 always 
    
    return n*fact(n-1) 
    
result = fact(6)

print(result)

