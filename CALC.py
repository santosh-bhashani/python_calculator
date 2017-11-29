def calcu():
    print("ENTER TWO NUMBERS YOU WANT TO OPERATE ON")
    a=int(input(""))
    b=int(input(""))
    print("CHOOSE THE OPERATION YOU WANT TO PERFORM")
    print("1 . TO ADD THE NUMBERS \n","2. TO SUBTRACT THE NUMBERS \n",'''3.TO DiVIDETHE NUMBERS \n''',"4.TO MULTIPLY THE NUMBERS" )
    n=int(input(""))
    if (n==1):
        sumu(a,b)
    elif (n==2):
        sub(a,b)
    elif (n==3):
        div(a,b)
    elif (n==4):
        mul(a,b)
    else:("choice doesnt exist")
    c=input("DO YOU WANT TO USE THE CALCULATOR AGAIN y/n \n")
    if (c=='y'or c=="Y"):
        calcu()
    else:
        ("THANKS FOR USING THE CALCULATOR")
    

def sumu(a,b):
    print("sum =",a+b)
def sub(a,b):
    print("SUB =",a-b)
def mul(a,b):
    print("MUL =",a*b)
def div(a,b):
    print("DIV=",a/b)
calcu()
