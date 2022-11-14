import os
print("Current Directory : ",os.getcwd())
print("1.Add Directory\n2.Remove Directory\n3.Change Directory : ")
cho=int(input("Enter the option : "))
if(cho==1):
    name=input("Enter Dir name : ")
    os.mkdir(name)
    print("After Adding Directory : ",os.listdir())
elif(cho==2):
    print("Directory list : ", os.listdir())
    name=input("Enter the dir name to remove : ")
    os.rmdir(name)
    print("After removing Directory : ",os.listdir())
elif(cho==3):
    print("Directory list : ", os.listdir())
    cname=input("Enter the Dir name to Change : ")
    name=input("Enter the new dir name to Change : ")
    os.rename(cname,name)
    print("After Changing Directory : ",os.listdir())
