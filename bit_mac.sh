#!/usr/bin/env bash

MAC_ADRESS_FILE="$HOME/Address_list.txt"

timestamp=$(date +"%y-%m-%d %H:%M:%S")


# Check if enough arguments are provided
if [ "$#" -gt 3 ]; then
  echo "Usage: $0 <network_interface> <MAC_address>"
  echo "Commands:"
  echo "Random: makes a random mac address and updates"
  exit 1
fi

# Capture the network interface and MAC address from arguments
network_interface="$1"
echo "Network Interface set to: $network_interface"

case "$2" in 
    random)
        mac_address=$(printf '02:%02X:%02X:%02X:%02X:%02X' $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)))
        echo "Random MAC Address generated: $mac_address"
        ;;
    *)
        mac_address="$2"
        echo "MAC Address set to: $mac_address"
        ;;
esac

# Validate the MAC address format
if [[ ! "$mac_address" =~ ^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$ ]]; then
  echo "Error: Invalid MAC address format."
  exit 2
fi

case "$3" in
    note)
        echo "[$timestamp] Net-interface: $network_interface MAC-address: $mac_address" >> "$MAC_ADRESS_FILE"
        ;;

    *)
        ;;
esac



# Bring the interface down
echo "Bringing down the interface: $network_interface"
sudo ip link set dev "$network_interface" down

# Set the new MAC address
echo "Setting MAC address to: $mac_address"
sudo ip link set dev "$network_interface" address "$mac_address"
echo "Mac Address saved in $MAC_ADRESS_FILE"

# Bring the interface back up
echo "Bringing up the interface: $network_interface"
sudo ip link set dev "$network_interface" up

# Display the updated network interface details
echo "Updated network interface details:"
ip link show dev "$network_interface"
