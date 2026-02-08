import sys

if len(sys.argv)<2:
    sys.exit("Too Few arguments")
elif len(sys.argv)>2:
    sys.exit("Too Much arguments")

print("hello, my name is",sys.argv[1])