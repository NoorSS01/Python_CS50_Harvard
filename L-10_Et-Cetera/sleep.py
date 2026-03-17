def main():
    n= int(input("Enter n :"))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock=[]
    for i in range(n):
        flock.append("🐑"* i )
    return flock
    #yield flock #this returns on every iteration

if __name__=="__main__":
    main()