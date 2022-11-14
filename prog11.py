class Employees():
    def Name(self):
        name=input("Enter the employee name : ")
        print("Employee Name:",name)
class salary(Employees):
    def gpay(self):
        bp=int(input("enter basic pay : "))
        hra = bp*10/100
        print("house rental allowance", hra)
        da=bp*5/100
        print("DA",da)
        gross=bp+hra+da
        print("gross pay",gross)
        return gross
class Designation(salary):
    def npay(self):
        lic=int(input("enter lic value : "))
        print("lic",lic)
        pf = int(input("enter provident fund : "))
        print("pf", pf)
        net=lic+pf
        print("netpay",net)
        return net
call = Designation()
call.Name()
a=call.gpay()
b=call.npay()
salary=a-b
print("employee salary",salary)