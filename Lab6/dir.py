#ex1
import os

def list_specific(path):
    
    directories = [item for item in os.listdir(path) if os.path.isdir(item)]

    files = [item for item in os.listdir(path) if os.path.isfile(item)]

    return directories, files

def list_all(path):
    
    all_directories = []
    all_files = []

    w=os.walk(path)

    for (p, d, f) in w:
        all_directories.extend(d)
        all_files.extend(f)
    return all_directories, all_files

path = 'C:\Users\user\Desktop\PP2\Lab6'

directories, files = list_specific(path)
print("Directories in this path:", directories)
print("Files in this path:", files)

all_directories, all_files = list_all(path)
print("All Directories in this path:", all_directories)
print("All Files in this path:", all_files)

#ex2
import os

def test_path(path):

    if not os.path.exists(path):
        print("Path does not exist.")
        return
    
    if not os.access(path, os.R_OK):
        print("Path is not readable.")
    else:
        print("Path is readable.")
    
    if not os.access(path, os.W_OK):
        print("Path is not writable.")
    else:
        print("Path is writable.")
    
    if not os.access(path, os.X_OK):
        print("Path is not executable.")
    else:
        print("Path is executable.")


path = 'C:\Users\user\Desktop\PP2\Lab6'

test_path(path)

#ex3
import os

def test_path(path):

    if not os.path.exists(path):
        print("Path does not exist.")
        return
    else:
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    



path = 'C:\Users\user\Desktop\PP2\Lab6'

test_path(path)

#ex4
def count_l(f):
    with open(f, "r") as file:
        num=0
        for line in file:
            num+=1
    return num


filename="C:\Users\user\Desktop\PP2\Lab6\4ex.txt"
print("num of lines:", count_l(filename))

#ex5
def aaa(f):
    listtof=[1, 2, 3]

    with open(f, "a") as file:
        file.write(", ".join(str(i) for i in listtof))


def bbb(f):
    with open(f, "r") as file:
        print(file.read())


filename="C:\Users\user\Desktop\PP2\Lab6\4ex.txt"
print("num of lines:", count_l(filename))

aaa(filename)

bbb(filename)

#ex6
import string

def ggg():
    for l in string.ascii_uppercase:
        filename = f"{l}.txt" 
        with open(filename, 'w') as file:
            file.write("blablabla")

ggg()

#ex7
def bbb(f):
    with open(f, "r") as file:
        bll=file.read()

    newf="newf.txt"

    with open(newf, "w") as file:
        file.write(bll)

bbb("C:\Users\user\Desktop\PP2\Lab6\4ex.txt")

#ex8
import os

file="C:\Users\user\Desktop\PP2\Lab6\4ex.txt"

def deletor(f):

    if not os.path.exists(f):
        print("path does not exist")
    else:
        if not os.access(f, os.X_OK):
            print("you do not have access to this file")
        else:
            os.remove(f)
            print("you have successfully deleted the file")
deletor(file)

