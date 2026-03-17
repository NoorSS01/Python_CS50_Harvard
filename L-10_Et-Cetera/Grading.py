def main():
    marking = get_int()
    grade = gradcal(marking)
    print(f"{marking} is {grade}")


def get_int():
    marks = int(input("Enter your Marks: "))
    return marks

def gradcal(marks):
    if marks > 90:
        return "Grade A"
    elif marks > 80:
        return "Grade B"
    elif marks > 70:
        return "Grade C"
    elif marks > 60:
        return "Grade D"
    elif marks > 50:
        return "Grade E"
    else:
        return "Grade F"

main()