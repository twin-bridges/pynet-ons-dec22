class NetworkDevice:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password


rtr1 = NetworkDevice(host="cisco3.lasthop.io", username="cisco", password="cisco")
print(rtr1)
