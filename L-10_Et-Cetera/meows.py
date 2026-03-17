import argparse

parser=argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", type=int, default=1)
args=parser.parse_args()

for _  in range(args.n):
    print("meow")