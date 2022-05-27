num=input("enter the number")
i=0
while i<len(num):
    if num[i]=="0":
        print("zero",end="")
    elif num[i]=="1":
        print("one",end="") 
    elif num[i]=="2":
        print("two",end="") 
    elif num[i]=="3":
        print("three",end="")
    elif num[i]=="4":
        print("four",end="")
    elif num[i]=="5" :
        print("five",end="")   
    elif num[i]=="6":
        print("six",end="") 
    elif num[i]=="7":
        print("seven",end="")  
    elif num[i] =="8":
        print("eight",end="")
    elif num[i]=="9":
        print("nine",end="") 
    else:
        print("nothing")
    i+=1                   
