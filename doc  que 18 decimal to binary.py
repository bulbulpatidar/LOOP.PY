a=int(input("enter the  decimal num:-"))
s=" "
while a>0:
    rem=str(a%2)
    a=a//2
    s+=rem
print(s[::-1])   
