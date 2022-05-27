from re import A


# A
# B B
# C C C 
# D D D D 
# E E E E E


a=65
i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(a),end=" ")
        j+=1
    print()
    i+=1
    a+=1    