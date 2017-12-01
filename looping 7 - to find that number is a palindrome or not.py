n=int(input("enter a number"))
s=0
a=n
r=0
while(n!=0):
    r=n%10
    s=s*10+r
    n=int(n/10)
if(a==s):
    print("the number is a palindrome")
else:
    print ("the number is not a palindrome")
    
    
