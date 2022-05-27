i=0
while i<=5:
    j=0
    while j<=6:
        if i==0 and j%3!=0 or i==1 and j%3==0 or i-j==2 or i+j==8:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1            