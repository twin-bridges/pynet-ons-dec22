import json
from rich import print

with open("get_hardware.json") as f:
    data = json.load(f)

print()
print(f"\nOur data structure has a type of: {type(data)}\n")

cameras = data["array"]
print("-" * 80)
for camera in cameras:
    print(f"Camera Display Name: {camera['displayName']}")

print("-" * 80)
