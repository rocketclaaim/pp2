#ex1
import math
degree=float(input('Input degree:'))
radian=math.radians(degree)
print('Output degree:',radian)

#ex2
import math
h=int(input('Height:'))
a=int(input('Base, first value:'))
b=int(input('Base, second value:'))
def trapezoid(a,b,h):
    S=(a+b)/2*h
    return S
S=trapezoid(a,b,h)
print('Expected Output:',S)

#ex3
import math
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
def area(n,s):
    S=(n * s**2) / (4 * math.tan(math.pi/n))
    return S
S=int(area(n,s))
print("The area of the polygon is:", S)

#ex4
import math
a=float(input('Length of base:'))
h=float(input('Height of parallelogram:'))
def parallelogram(a,h):
    S=a*h 
    return S
S=parallelogram(a,h)
print('Expected Output:',S)

