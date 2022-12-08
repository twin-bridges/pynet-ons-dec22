from rich import print

net_devices = {}
chi_rtr1 = {
    "ip_addr": "172.30.220.1",
    "username": "admin",
    "password": "some_pass",
    "vendor": "cisco",
    "model": "3945",
}
chi_rtr2 = {
    "ip_addr": "172.30.220.2",
    "username": "admin",
    "password": "pass2",
    "vendor": "cisco",
    "model": "3945",
}
net_devices["chi_rtr1"] = chi_rtr1
net_devices["chi_rtr2"] = chi_rtr2
print(net_devices)
