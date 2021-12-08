#! /usr/bin/env python

#Construct a function that has three parameters x, y, z
#z has a default value of 20
#Return x + y + z
#Call this function using all three positional arguments
#Call this function using named arguments x, y (let z be the default)
#Call this function with one positional argument and two named arguments.
#Call this function using three strings.
#Call this function using three lists.

def myfunc(x, y, z=20): 
    return x + y + z
print()
return_val = myfunc(1, 2, 3)
print(f"Calling 3 positional arguments: {return_val}")

return_val = myfunc(x=1, y=2)
print(f"Calling with two named args:: {return_val}")

return_val = myfunc(10, z=3, y=2)
print(f"Calling with one positional and two named args: {return_val}")

return_val = myfunc(x="x", y="y", z="z")
print(f"Calling with three strings: {return_val}")

return_val = myfunc(x=["x"], y=["y"], z=["z"])
print(f"Calling with three lists: {return_val}")
print()
