num=int(input("enter the number"))
org=num
sum=0
while num>0:
    sum=sum+num%10
    num=num//10
print(sum)
if org%sum==0:
    print("harshad number") 
else:
    print("not harshad number")       