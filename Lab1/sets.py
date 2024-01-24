#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
   print("Yes, apple is a fruit!")

#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") #дискард удаляет элемент в множестве если он есть

