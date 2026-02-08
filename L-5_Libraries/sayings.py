def main():
    name=input("Enter your name :")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

def goodbye(to="world"):
    return f"goodbye, {to}"


if __name__=="__main__":
    main()