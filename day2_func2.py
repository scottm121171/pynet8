#! /usr/bin/env python

#Functions Ex2
#--------------

#Expand on functions exercise 1.

#a. Create a list with three numbers
#b. Use *args to call the function
#c. Create a dictionary that has three keys of x, y, and z
#d. Call the functions using **kwargs
def my_func(x, y, z=20):
    return x + y + z

my_list = [
    1,
    2,
    3
]

my_dict = {"x": 13, "y": 22, "z": 1}

print()
return_val = my_func(10, 20, 30)
print(f"Calling with three positional args: {return_val}")

return_val = my_func(x=10, y=20)
print(f"Calling with two named args: {return_val}")

return_val = my_func(10, z=13, y=20)
print(f"Calling with one positional and two named args: {return_val}")

return_val = my_func(x="x", y="y", z="z")
print(f"Calling with three strings: {return_val}")

return_val = my_func(x=["x"], y=["y"], z=["z"])
print(f"Calling with three lists: {return_val}")

return_val = my_func(*my_list)
print(f"Calling with *args: {return_val}")

return_val = my_func(**my_dict)
print(f"Calling with **kwargs: {return_val}")
print()
