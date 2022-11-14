class employee:
    grosspay=0
    salary=0
    def details(self):
        empid=input("enter the employee id:")
        empname=input("enter employee name:")
    def gross(self):
        employee.salary = int(input("enter your salary:"))
        da=employee.salary*5/100
        print("DA:",da)
        hra=employee.salary*10/100
        print("HRA:",hra)
        employee.grosspay=employee.salary+da+hra
        print("grosspay:",employee.grosspay)
        return employee.grosspay
    def netpay(self):
        it=employee.salary*7/100
        print("IT:",it)
        pf = employee.salary * 12/ 100
        print("PF:", pf)
        netpay=employee.grosspay-pf-it
        print("NETPAY:",netpay)
s= employee()
s.details()
s.gross()
s.netpay()