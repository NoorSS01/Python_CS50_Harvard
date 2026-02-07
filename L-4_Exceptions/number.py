## Handling Errors :
# try, except, else
# while True:
#     try:
#         x=int(input("Enter x :"))
#         print("x is integer")
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

# try, except, else using functions
def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x=int(input("Enter x :"))
        except ValueError:
            # pass
            print("x is not an integer")
        else:
            return x
main()