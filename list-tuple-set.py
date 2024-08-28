#List [] = mutable, most flexible

fruits = ["apple","orange","banana","coconut"]

fruits[0]= "pineapple"
fruits.append("melon")
# fruits.remove("banana")
# fruits.pop(0) // removes [0]
# fruits.clear() //clears the list

for fruit in fruits:
    print(fruit, end=" ")

#Tuple () = immutable, faster
salads = ("domatoes","cucumber","carrot","iceberg")

# salad.remove("carrot") 
# tuple object can't be removed. 

for salad in salads:
    print(salad)

#Set {} = mutable (add/remove), unordered, no dublicates, best for membership testing

colors = {"red", "yellow", "green", "blue"} # colors = {"red", "yellow", "green", "blue", "blue", "blue"} would result in red yellow green blue // no duplicate blue

color = input("Enter a color to search for: ")
# color[0] = "orange"
# set objects does not support item assignment

colors.add("pink")
colors.remove("red")
# colors.pop(0) // set.pop() takes no arguments (1 given)

#for color in colors:
 #   print(color)

if color in colors:
    print(f"{color} is found")  # example for membership testing
else:
    print(f"{color} is not found")