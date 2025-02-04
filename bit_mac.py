
import sys
import os
import re
import random
import subprocess
from datetime import datetime

def generate_random_mac():
    #Generate a random MAC address with the first octet set to 02.
    return "02:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}".format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def print_usage(script_name):
    """Prints the usage information for the script."""
    print(f"Usage: {script_name} <network_interface> <MAC_address/random> [note]")
    print("Commands:")
    print("  random: makes a random MAC address and updates")
    sys.exit(1)

def main():
    # Check the number of command-line arguments (excluding the script name)
    args = sys.argv[1:]
    if len(args) > 3 or len(args) < 2:
        print_usage(sys.argv[0])

    # Extract arguments
    network_interface = args[0]
    mac_input = args[1]

    print(f"Network Interface set to: {network_interface}")

    # Determine whether to generate a random MAC address or use the provided one
    if mac_input.lower() == "random":
        mac_address = generate_random_mac()
        print(f"Random MAC Address generated: {mac_address}")
    else:
        mac_address = mac_input
        print(f"MAC Address set to: {mac_address}")

    # Validate MAC address format (must be 6 groups of 2 hex digits separated by ':')
    if not re.fullmatch(r'([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}', mac_address):
        print("Error: Invalid MAC address format.")
        sys.exit(2)

    # If a third argument is provided and equals 'note', log the change
    if len(args) == 3 and args[2].lower() == "note":
        timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        mac_address_file = os.path.join(os.path.expanduser("~"), "Address_list.txt")
        try:
            with open(mac_address_file, "a") as f:
                f.write(f"[{timestamp}] Net-interface: {network_interface} MAC-address: {mac_address}\n")
            print(f"MAC Address saved in {mac_address_file}")
        except Exception as e:
            print(f"Error writing to log file: {e}")

    # Bring the interface down
    print(f"Bringing down the interface: {network_interface}")
    subprocess.run(["sudo", "ip", "link", "set", "dev", network_interface, "down"], check=True)

    # Set the new MAC address
    print(f"Setting MAC address to: {mac_address}")
    subprocess.run(["sudo", "ip", "link", "set", "dev", network_interface, "address", mac_address], check=True)

    # Bring the interface back up
    print(f"Bringing up the interface: {network_interface}")
    subprocess.run(["sudo", "ip", "link", "set", "dev", network_interface, "up"], check=True)

    # Display the updated network interface details
    print("Updated network interface details:")
    subprocess.run(["ip", "link", "show", "dev", network_interface], check=True)

if __name__ == "__main__":
    main()