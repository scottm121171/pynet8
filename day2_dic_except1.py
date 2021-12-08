#!/usr/bin/env python

#Dict Ex2
#---------
#
#Expand on dictionary exercise1.
#
#Try to retrieve the ‘device_type’ just by directly accessing the key.
#Gracefully, handle the exception and print the message that the device_type 
#field is not found.






net_device = {
    "ip_addr": "172.30.220.1",
    "username": "admin",
    "password": "some_pass",
    "vendor": "cisco",
    "model": "3945",
}

print()
for k, v in net_device.items():
    print(k, v)

net_device["password"] = "new_value"
net_device["secret"] = "some_secret"

device_type = net_device.get("device_type", "cisco_ios")
print("\nDefault device type: {}\n".format(device_type))

try:
    device_type = net_device["device_type"]
except KeyError:
    print("Device type not found\n")
