ans = "y"
while (ans == "y" or ans == "Y"):
    name = input("enter the string:")
    print("1.capatilize()")
    print("2.casefold()")
    print("3.isprintable")
    print("4.isaplha()")
    print("5.lower()")
    print("6.upper()")
    print("7.center()")
    print("8.encode()")
    print("9.isdigit()")
    print("10.isupper()")
    choice = int(input("enter your choice:"))
    if choice == 1:
        a = name.capitalize()
        print(a)
    elif choice == 2:
        b = name.casefold()
        print(b)
    elif choice == 3:
        c = name.isprintable()
        print(c)
    elif choice == 4:
        d = name.isalpha()
        print(d)
    elif choice == 5:
        e = name.lower()
        print(e)
    elif choice == 6:
        f = name.upper()
        print(f)
    elif choice == 7:
        g = name.center()
        print(g)
    elif choice == 8:
        h = name.encode()
        print(h)
    elif choice == 9:
        i = name.isdigit()
        print(i)
    elif choice == 10:
        j = name.isupper()
        print(j)
    ans = input("do you want to continue(y/n)")
