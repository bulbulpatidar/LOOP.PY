n=int(input("enter the number"))
s=0
i=1
while i<=n:
    wt=int(input("enter the num"))
    s=s+wt
    i+=1
avg=s/n
print("average",avg)
if avg%5==0:
    print("multiple of 5",avg) 
else:
    print("not multiple of 5 ",avg)       