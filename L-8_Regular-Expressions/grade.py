score=int(input("Enter your Score :"))

if(score>=90):
    print(f"{score} is Grade A")
elif(score>=80):
    print(f"{score} is Grade B")
elif(score>=70):
    print(f"{score} is Grade C")
elif(score>=60):
    print(f"{score} is Grade D")
else:
    print(f"{score} is Grade F")