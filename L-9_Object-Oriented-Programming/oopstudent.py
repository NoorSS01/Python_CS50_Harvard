# def main():
#     students=get_students()
#     if students["name"]=="Padma":
#         students["house"]="Ravenclaw"
#     print(f"{students['name']} from {students['house']}") #indexing by TUPLE

# def get_students():
#     name=input("Enter name:")
#     house=input("Enter house:")
#     return {"name":name, "house":house}       #Returning Dictionary, Mutable
# #    return [name, house]                     #Returining List, Mutable
# #    return (name, house)                     #Returning TUPLE, Immutable

# if __name__=="__main__":
#     main() 

# Using Classes
class Student:
    def __init__(self, name, house):
        self.name=name
        self.house=house

    def __str__(self):
        return (f"{self.name} from {self.house}")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name=name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house=house


def main():
    student=get_student()
    student.name="Haryyy"
    print(student)

def get_student():
    name=input("Enter student :")
    house=input("Enter house :")
    try:
        return Student(name, house)
    except ValueError:
        ...

if __name__=="__main__":
    main()