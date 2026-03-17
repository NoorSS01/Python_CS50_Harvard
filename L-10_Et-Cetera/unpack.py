def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins=[2,6,4]

print(total( *coins), "Knuts") #unpacking

def f(*args, **kwargs):
    print("Positional:", args)
    # print("Positional:", kwargs)

f(100, 50, 25)
# f(galleons=100, sickles=50, knuts=25)