#! /usr/bin/env python

my_list = [ 
    "Hello",
    "Hello1",
    "Hello2",
    "Hello3",
    "Hello4",
    "Hello5",
    "Hello6",
]

for my_var in my_list:
    print(my_var)

for i in range(len(my_list)):
    print (i)
    print(my_list[i])

for i, my_list in enumerate(my_list):
    print(i)
    print(my_var)
