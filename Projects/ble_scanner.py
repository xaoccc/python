# pip install bleak
import asyncio
from bleak import BleakScanner, BleakClient


async def scan_for_devices(timeout=10):
    devices = await BleakScanner.discover(timeout)
    return devices

my_devices = {
    "relay": "34:85:18:DF:19:F6",
    "button": "5C:C7:C1:F1:50:7A",
}
async def main():
    devices = await scan_for_devices()
    print("Discovered devices:")
    for device in devices:
        if device.address == my_devices["relay"]:
            selected_device = device
            print(dir(device))
            print("Name:", device.name)
            print("Address:", device.address)
            # print("Meta:", device.metadata)
            # print("RSSI:", device.rssi)
            print("repr:", device.__repr__())


    print(f"Selected device: {selected_device.name} [{selected_device.address}]")
    address = my_devices["relay"]

    # Step 2: Connect to the selected device
    async with BleakClient(address) as client:
        print(f"Connected to {selected_device.name} [{address}]")

        # Step 3: Interact with the device's services and characteristics
        services = client.services
        print("Available Services:")
        for service in services:
            print(f"[Service] {service.uuid}: {service.description}")
            for char in service.characteristics:
                print(f"  [Characteristic] {char.uuid}: {char.description}")

                # Read characteristic value (if readable)
                if 'read' in char.properties:
                    value = await client.read_gatt_char(char.uuid)
                    print(f"    Value: {value}")


if __name__ == "__main__":
    asyncio.run(main())



