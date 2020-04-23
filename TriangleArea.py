# Triangle Area Finder

a = float(input("Enter the one side")) # we can use int as it gives same result
b = float(input("Enter the second side"))
c = float(input("Enter the third side"))
s = (a+b+c)/2  # formula to find area

  area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    print ("The area of triangle is area ", area)




