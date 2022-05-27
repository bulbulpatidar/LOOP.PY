
# n=int(input("enter the number:-"))
a=1
i=1
while i<=3:
    b=1
    while b<=3-i:
        print(" ",end=" ")
        b+=1
    j=1
    while j<=a:
        print("*",end=" ")
        j+=1
    print()
    i+=1
    a+=2  
a=3
i=3
while i>=1:
    b=1
    while b<=4-i:
        print(" ",end=" ")
        b+=1
    j=1
    while j<=a:
        print("*",end=" ")
        j+=1
    print()
    i-=1
    a-=2                 

