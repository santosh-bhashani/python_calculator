n=int(input("enter a no."))
if(n<=1):
    print("the no. is not prime")
i=2
c=0
while(i<n):
    n=n%i
    if(n==0):
        c=1
        i=i+1
if(c==0):
    print("the no. is prime")
else:
    print("the no. is not prime")
          
