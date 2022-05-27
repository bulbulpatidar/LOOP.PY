# 1+2+6+24+120......


n=int(input("enter the number"))
sum=0
i=1
p=1
while i<=n:
    p=p*i 
    print(p,end="+")
    sum=sum+p
    i+=1
print() 
print(sum)   