def main():
    x=int(input("Enter x :"))
    if even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def even(n):
    # return True if n%2==0 else False
    return n%2==0

main()