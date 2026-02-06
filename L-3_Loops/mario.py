# Mario Game Block
# def main():
#     print_column(3)
# def print_column(height):
#     print("#\n" * height, end="")
# main()

# Mario mystery blocks
# def main():
#     print_row(4)
# def print_row(width):
#     print("?"*width)
# main()

# Mario 3x3 Block
def main():
    print_square(3)
def print_square(size):
    for i in range(size):
    #     for j in range(size):
    #         print("#", end="")
    #     print()
        print("#" * size)
main()