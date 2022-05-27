i=1
while i<=5:
    j=1
    while j<=5:
        if i+j==4 or i-j==2 or i+j==8 or j-i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1            

