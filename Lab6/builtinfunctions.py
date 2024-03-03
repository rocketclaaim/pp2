#ex1
#import functools
import operator
n=int(input())
my_list=[]
for i in range(n):
    element=int(input())
    my_list.append(element)
result=functools.reduce(operator.mul,my_list)
print(result)

#ex2
import functools
import operator
s=input()
upper=0
lower=0
for char in s:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
print(upper)
print(lower)

#ex3
import string
s=input()
d=''.join(reversed(s))
if s==d:
    print('palindrome')
else :
    print('no')

#ex4
import time
n=int(input())
a=int(input())
time.sleep(a/1000)
print("Square root of",n, "after 2123 miliseconds is ",n**0.5)

#ex5
import operator
import functools
t=input()
my_tuple=tuple(map(int,t.split()))
print(all(my_tuple))




