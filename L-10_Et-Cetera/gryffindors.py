students=[
    {"Name":"Harry", "House":"Gryffindor"},
    {"Name":"Hermione", "House":"Gryffindor"},
    {"Name":"Ron", "House":"Gryffindor"},
    {"Name":"Draco", "House":"Slytherin"},
    {"Name":"Padma", "House":"RavenClaw"},
]

def is_gryffindor(s):
    return s["house"]== "Gryffindor"

gryffindors= filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["Name"]):
    print(gryffindor["Name"])
    