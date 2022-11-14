department = {
    "name": "SURYA",
    "rollno": "18mss000",
    "age": 21
}
print(department)
print("1.adding")
print("2.changing")
print("3.length")
print("4.DELETE")
print("5.key elements")
choice = int(input("enter your choice:"))
if choice == 1:
    print("ADDING ELEMENTS TO DICTIONARY:")
    department["gender"] = "male"
    print(department)
elif choice == 2:
    print("CHANGING ELEMENTS IN DICTIONARY:")
    a = input("enter the age to be inserted:")
    department["age"] = a
    print(department)
elif choice == 3:
    print("LENGTH OF THE DICTIONARY:")
    print(len(department))
elif choice == 4:
    print("DELETNG ELEMENTS IN DICTIONARY:")
    department.pop("rollno")
    print(department)
elif choice == 5:
    print("DISPLAYING ALL kEY ELEMENTS IN DICTIONARY:")
    print(department.keys())
