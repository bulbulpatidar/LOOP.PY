print("guessing game")
print("guessing the number 1 to 10")
i=1
while i<=5:
    num=int(input("enter the number"))
    if num==5:
        print("congratulation you win the game")
        break
    else:
        print("guess again")
    i+=1
if i>5:
    print("sorry you loss the game")        