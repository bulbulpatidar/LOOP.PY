n=(input("enter the string ;"))
i=0
while i<len(n):
    j=0
    while j<=i:
        print(n[j],end=" ")
        j+=1
    print()
    i+=1     