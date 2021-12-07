#! /usr/bin/env python
# define list
list = [
    "red",
    "blue",
    "orange",
    "yellow",
    "brown"
]
#loop through to display for user
for my_var in list:
    print(my_var)
#Ask for user input
print("Let's add two new colors.")
v1 = input("Please enter 1st new color:    ")
v2 = input("Please enter 2nd new color:    ")
#capture the varible
list.append(v1)
list.append(v2)
#display added input from user appended
for my_var in list:
    print(my_var)
#give the new count
print ("number of items in this list and sorting alphabettically:", len(list)) 
#sort alphabetically 
list.sort()
print(list)
#end of script

