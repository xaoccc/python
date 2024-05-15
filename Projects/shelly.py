import requests

shelly_ip = "192.168.0.28"
shelly_url = f"http://{shelly_ip}/relay/0"

try:
    if requests.get(shelly_url).json()['ison']:
        response = requests.get(f"{shelly_url}?turn=off")
        print("Relay turned off successfully.")
    else:
        response = requests.get(f"{shelly_url}?turn=on")
        print("Relay turned on successfully.")
except requests.exceptions.RequestException as e:
    print(f"Failed to turn on relay: {e}")

try:
    # Get relay status
    response = requests.get(shelly_url)
    response.raise_for_status()
    print("Relay status:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Failed to get relay status: {e}")


def get_device_info(ip):
    url = f"http://{ip}/shelly"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get device info: {e}")
        return None

device_info = get_device_info(shelly_ip)
if device_info:
    print("Device Information:")
    print(device_info)
