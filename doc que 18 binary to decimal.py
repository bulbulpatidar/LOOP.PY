n=int(input("enter the number"))
i=0
sum=0
while n>0:
    sum=sum+(n%10)*(2**i)
    n=n//10
    i+=1
print(sum)    


