# pip install pybluez2
import bluetooth


def discover_devices():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=True)
    return nearby_devices


if __name__ == "__main__":
    print("Scanning for nearby Bluetooth devices...")
    nearby_devices = discover_devices()

    print("Found %d devices:" % len(nearby_devices))
    for device_data in nearby_devices:
        print(f"address: {device_data[0]}, name: {device_data[1]}")

