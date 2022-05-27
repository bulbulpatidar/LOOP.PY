# 1+4-9+16-25+36-49+....n
n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    if i==n:
        print(i**2)
    elif i%2==0:
        print(i**2,end="-") 
    else:
        print(i**2,end="+")
    sum+=i**2
    i+=1
print() 
print(sum)              
