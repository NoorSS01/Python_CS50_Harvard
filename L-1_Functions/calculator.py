def main():
    x=int(input("Enter x value :"))
    print(f"Square of {x} is",square(x))

def square(n):
    return n**2

if __name__=="__main__":
    main()