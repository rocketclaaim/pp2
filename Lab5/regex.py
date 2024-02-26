#ex1
import re
s=r'ab*'
a=input()
if re.match(s,a):
    print('matched')
else:
    print("doesn't matched")

#ex2
import re
s=r'ab{2,3}*'
a=input()
if re.match(s,a):
    print('matched')
else:
    print("doesn't matched")

#ex3
import re
s=r'[a-z_]+'
a=input()
if re.match(s,a):
    print('matched')
else:
    print("doesn't matched")

#ex4
import re
s=r'[A-Z][a-z]+'
a=input()
if re.match(s,a):
    print('matched')
else :
    print("doesn't matched")

#ex5
import re
s=r"a[a-zA-Z-_0-9]*b"
a=input()
if re.match(s,a):
    print('matched')
else:
    print("doesn't matched")

#ex6
import re
s=r'[,.]+'
a=':'
b=input()
result=re.sub(s,a,b)
print(result)

#ex7
import re
s=input()
ss=re.split('_',s)
sss=""
for i in ss:
    sss+=ss.capitalize()
print(sss)

#ex8
import re
s=input()
ss=re.split("[A-Z]",s)
sss=""
for i in ss:
    sss+=sss+""+i
print(sss)

#ex9
import re
s=r"\w"
ss=input("enter a string: ")
sss=re.findall(pat, ss)

a=""

for i in x:
    if i.isupper():
        a+=" "+i
    else:
        a+=i

print(a)

#ex10
import re
s=input("enter a string: ")
new_s=""
pat=r"\w"
x=re.findall(pat, s)
for i in x:
    if i.isupper() and i!=x[0]:
        new_s+="_"+i
    else:
        new_s+=i
print(new_s)