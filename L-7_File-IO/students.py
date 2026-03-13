import csv

# #READ & Print names from CSV
# students=[]

# with open("students.csv") as file:
#     for line in file:
#         name, house =line.rstrip().split(",")
#         student={"name":name, "house":house}
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# # Faster Approach to READ & Print names from CSV
# students=[]

# with open("students.csv") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         students.append(row)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# # WRITE or APPEND in CSV
# name=input("Enter name :")
# home=input("Enter home :")

# with open("students.csv", "a") as file:
#     writer=csv.writer(file)
#     writer.writerow([name, home])
