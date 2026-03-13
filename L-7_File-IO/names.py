# # WRITE or APPEND and SAVE in files
# name=input("Enter the Name :")
# with open("names.txt", "a") as file:
#     file.write(f"{name}")


# # READING the files
# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")

# READING and SORTING
names=[]

with open("names.txt") as file: #"r" is default in python
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")