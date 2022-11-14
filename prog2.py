print("1.EVEN\n2.ODD")
choice = (int(input("your choice:")))
if choice == 1:
    a = 1
    while a < 10:
        if a % 2 == 0:
            print(a)
        a = a+1
elif choice == 2:
    num = int(input("num:"))
    for x in range(1, num+1):
        if x % 2 != 0:
            print(x)
