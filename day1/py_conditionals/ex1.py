ip_addr = input("\nEnter an IP address: ")

if "192.168" in ip_addr:
    print("\nThe IP Address is correct\n")
else:
    print(f"\nInvalid IP Address: {ip_addr}\n")