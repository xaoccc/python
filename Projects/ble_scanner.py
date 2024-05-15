# pip install bleak
import asyncio
from bleak import BleakScanner, BleakClient


async def scan_for_devices(timeout=10):
    devices = await BleakScanner.discover(timeout)
    return devices

async def main():
    devices = await scan_for_devices()
    print("Discovered devices:")
    for device in devices:
        if device.address == "5C:C7:C1:F1:50:7A":
            print(dir(device))
            print("Name:", device.name)
            print("Address:", device.address)
            print("Meta:", device.metadata)
            print("RSSI:", device.rssi)
            print("repr:", device.__repr__())

    device_index = int(input("Select a device by its index: "))
    selected_device = devices[device_index]
    address = selected_device.address

    # Step 2: Connect to the selected device
    async with BleakClient(address) as client:
        print(f"Connected to {selected_device.name} [{address}]")

        # Step 3: Interact with the device's services and characteristics
        services = await client.get_services()
        print("Available Services:")
        for service in services:
            print(f"[Service] {service.uuid}: {service.description}")
            for char in service.characteristics:
                print(f"  [Characteristic] {char.uuid}: {char.description}")

                # Read characteristic value (if readable)
                if 'read' in char.properties:
                    value = await client.read_gatt_char(char.uuid)
                    print(f"    Value: {value}")

async def connect_to_device():
    device_address = "42:A8:A4:E1:BB:36"  # Replace with the address of your BLE device

    async with BleakClient(device_address) as client:
        await client.connect()  # Connect to the BLE device
        print("Connected to device:", device_address)

        services = await client.get_services()  # Retrieve the services offered by the BLE device
        print(services)

        value = await client.read_gatt_char('0000fd69-0000-1000-8000-00805f9b34fb')
        print("Value read from characteristic:", value)

        await client.disconnect()  # Disconnect from the BLE device
        print("Disconnected from device:", device_address)

if __name__ == "__main__":
    asyncio.run(main())



