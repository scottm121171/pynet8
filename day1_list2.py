#! /usr/bin/env python

v1 = input("Please enter the IP address:    ")

print(f"{v1:12}")

oct1, oct2, oct3, oct4 = v1.split('.')
print(f"{oct1:<12} {oct2:<12} {oct3:<12} {oct4:<12}")
# to create a column 
#print(f"{oct1:<12}")
#print(f"{oct2:<12}")
#print(f"{oct3:<12}")
#print(f"{oct4:<12}")

list = [
    oct1, 
    oct2, 
    oct3, 
    oct4
]

for my_var in list:
    print(my_var)

print(f'{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}')
oct4 = 0
print(oct4)

print(f"{oct1:<12} {oct2:<12} {oct3:<12} {oct4:<12}", '{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}')
