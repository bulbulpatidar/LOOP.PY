# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1
i=5
while i>=1:
    b=1
    while b<=5-i:
        print(" ",end=" ")
        b+=1
    j=1
    while j<=i:
        print(j,end=" ") 
        j+=1
    print()
    i-=1       