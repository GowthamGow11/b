m1=int(input("mark 1:"));
m2=int(input("mark 2:"));
m3=int(input("mark 3:"));
total=int(m1+m2+m3);
print("total marks:",total);
average=total/3;
print("average" ,average);
if average>50:
    print("good in average");
elif average<50:
    print("try to get more average m");
else:
 print("sorry");