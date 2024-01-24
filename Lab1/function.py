#ex1
def my_function():
 print("Hello from a function")

#ex2
def my_function():
  print("Hello from a function")

my_function()

#ex3
def my_function(fname, lname):
  print(fname)

#ex4
def my_function(x):
  return x+5

#ex5
def my_function(*kids):
  print("The youngest child is " + kids[2]) #*-бесконечное количество аргументов,которые будут переданы в функцию

#ex6
def my_function(**kid):
  print("His last name is " + kid["lname"]) #**-бесконечное количество аргументов ключевых,которые будут переданы в функцию

