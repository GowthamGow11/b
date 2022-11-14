f1 = open("mytext.txt", "w")
data = input("enter the data")
f1.write(data)
f1 = open("mytext.txt", "r")
result = f1.read()
print("original file contents:", result)
f2 = open("copy.txt", "w")
with open("mytext.txt", "r")as fil:
    for f in fil:
        f2.write(f)
        f2 = open("copy.txt", "r")
        result1 = f2.read()
        print("copied file content:", result1)
        f2.close()