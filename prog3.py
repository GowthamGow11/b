print("1.SQUARE \n2.RECTANGLE")
choice = int(input("enter the choice:"))
if choice == 1:
    r = (int(input("Please enter the side of square:")))
    def square(r):
       return r*r
    print("area of square:", square(r))
elif choice == 2:
    b = (int(input("Please enter the Breath of the rectange:")))
    l = (int(input("Please enter the Length of the rectange:")))
    def rectangle(b, l):
        area = b*l
        print("area of rectangle is:", area)
    rectangle(b, l)
