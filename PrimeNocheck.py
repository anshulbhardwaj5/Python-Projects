print"We will check which is prime num and which is even num...!!"
pnum = int(input("Enter a number..."))
nume = int(input("Enter a number..."))
for i in range (2, pnum):
    if pnum % i ==0:
        print "Number is not Prime"
        break
else:
    print "Prime Number is",pnum

if nume % 2==0: #We are also checking even no with prime number
    print"Even Number is",nume

else:
    print"Number is not Even",nume