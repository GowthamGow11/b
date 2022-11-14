print("1.built in 2.user defined")
cho=int(input("enter your choice"))
if cho==1:
    x = int(input("enter the number"))
    if x < 0:
       raise Exception("Sorry, no numbers below zero")
    else:
        print(x)
elif cho==2:
    class Error(Exception):
        pass
    class valueerr(Error):
        pass
    try:
        age = int(input("enter age"))
        print("Age is:")
        print(age)
        if age < 0:
            raise valueerr
        yearOfBirth = 2022 - age
        print("Year of Birth is:")
        print(yearOfBirth)
    except valueerr:
        print("Input Correct age.")
