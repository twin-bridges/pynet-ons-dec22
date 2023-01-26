# b. Assign it an ip address, a username, a password, a vendor, and a model
#   field: ip_addr, username, password, vendor, model.
from rich import print

chi_rtr1 = {
    "ip_addr": "10.1.1.1",
    "username": "admin",
    "password": "bogus",
    "vendor": "aruba",
    "model": "Aruba-CX",
}

chi_rtr2 = {
    "ip_addr": "10.1.1.2",
    "username": "admin",
    "password": "bogus",
    "vendor": "aruba",
    "model": "Aruba-CX",
}

net_devices = {
    "chi_rtr1": chi_rtr1,
    "chi_rtr2": chi_rtr2,
}
# net_devices["chi_rtr1"] = chi_rtr1
# net_devices["chi_rtr2"] = chi_rtr2

print(net_devices)
