# List
# students=["Hermione", "Harry", "Ron"]
# for i in range(len(students)):
#     print(i+1, students[i])

# Dictionary (Dict)
# students={
#     "Hermione":"Gryffindor",
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco":"Slytherine",
# }
# for student in students:
#     print(student, students[student], sep=", ")

# List of Dictionaries (Dict)
students=[
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russel Terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")