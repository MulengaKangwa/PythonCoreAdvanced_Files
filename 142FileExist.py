import os,sys

if os.path.isfile("myfile.txt"):
    f = open("myfile.txt","r")
else:
    print("This file does not exist")
    sys.exit()
s=f.read()
print(s)
f.close()

