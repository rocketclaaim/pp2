#ex1
class Strings:
   ##   self.str = str(input())
    
    def print_string(self):
        print('cbcb')


p1=Strings()
p1.print_string()

#ex2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        return self.lenght * self.lenght


s = Square(int(input()))

print("Area of the square:", s.area())

#ex3
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width


    def area(self):
        return self.lenght * self.width


s = Rectangle(10, 3)

print("Area of the rectangle:", s.area())

#ex4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f'Coordinates {self.x}, {self.y}')
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point(1, 2)
p2 = Point(4, 6)


p1.show()
p2.show()


p1.move(3, 4)
p2.move(-3, -4)


print("Point 1 after moving:")
p1.show()
print("Point 2 after moving:")
p2.show()


print("Distance between the points:", p1.dist(p2))

#ex5
class Account: 
    def __init__(self, owner, balance): 
        self.owner = owner 
        self.balance = balance 
        pass 
 
 
    def deposit(self): 
        self.depo = int(input()) 
        self.balance += self.depo 
 
    def withdraw(self, sum): 
        self.min = sum 
        print(f'Напоминание: Вы не можете снять более чем {self.balance} тенге') 
        if self.min > self.balance: 
            print("Error, limit") 
        elif self.balance - self.min < 0: 
            print("Error") 
        else:  
            self.balance -= self.min 
            print (f'Ostatok:{self.balance}') 
         
 
Bank1 = Account('Alibaba', 100000) 
 
min = int(input()) 
Bank1.withdraw(min)