# import socket
#
# adapter_addr = 'ac:74:b1:bd:5d:2f'
# port = 7  # Normal port for rfcomm?
# buf_size = 1024
#
# s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
# s.bind((adapter_addr, port))
# s.listen(1)
# try:
#     print('Listening for connection...')
#     client, address = s.accept()
#     print(f'Connected to {address}')
#
#     while True:
#         data = client.recv(buf_size)
#         if data:
#             print(data)
# except Exception as e:
#     print(f'Something went wrong: {e}')
#     client.close()
#     s.close()

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

