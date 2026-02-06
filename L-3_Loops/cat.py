# While Loop
# i =0
# while i<5:
#     print("meow")
#     i += 1

# For Loop
# for _ in range(3):
#     print("meow")

# Just a Python feature
# print("meow\n" * 3) #at end it will take extra blank space
# print("meow\n" * 3, end="")

# Different Approach
# while True:
#     n=int(input("Enter n :"))
#     if n>0:
#         break
# for _ in range(n):
#     print("meow")


#Using functions
def main():
     number=get_number()
     meow(number)

def get_number():
    while True:
        n=int(input("Enter n :"))
        if n > 0:
            break
    return n

def meow(n):
     for _ in range(n):
        print("meow")

main()