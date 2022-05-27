# A
# A B 
# A B C 
# A B C D 
# A B C D E
i=1
while i<=5:
    a=65
    j=1
    while j<=i:
        print(chr(a),end=" ")
        j+=1
        a+=1
    print()
    i+=1    