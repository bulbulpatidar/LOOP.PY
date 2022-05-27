n=int(input("enter the number"))
count=0
i=1
while i<=n:
    if n%i==0:
        count=count+1
    i+=1
if count==2:
    print("prime number")
else:
    print("not prime number")            


# n=int(input("enter the number"))
# num=2
# while num<n:
#     if n%num==0:
#         print("not a prime number")
#         break
#     elif (n-1)==num:
#         print(n,"prime number")
#     num+=1    