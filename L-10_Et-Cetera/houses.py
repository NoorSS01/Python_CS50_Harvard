# 1.
students=[
    {"Name":"Harry", "House":"Gryffindor"},
    {"Name":"Hermione", "House":"Gryffindor"},
    {"Name":"Ron", "House":"Gryffindor"},
    {"Name":"Draco", "House":"Slytherin"},
    {"Name":"Padma", "House":"RavenClaw"},
]

# 2.
houses=set()

# 3.
for student in students:
    houses.add(student["House"])
for house in sorted(houses):
    print(house)