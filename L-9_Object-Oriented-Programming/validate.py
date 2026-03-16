import re

email=input("Enter you email :").strip()

if re.search(r"\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")