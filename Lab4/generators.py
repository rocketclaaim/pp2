#ex1
def square(a):
    for i in range(1, a + 1):
        yield i**2
a=int(input())
print(list(square(a)))

#ex2
def even(n):
    for i in range(0,n+1,2):
        yield i
        
n=int(input())
result=','.join(map(str,even(n)))
print(result)

#ex3
def div(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
print(list(div(n)))

#ex4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
print(list(squares(a,b)))

#ex5
def zero(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
print(list(zero(n)))