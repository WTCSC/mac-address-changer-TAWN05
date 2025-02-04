# **Bit_MAC.sh**

## **Description**

`bit_mac.sh` is a Bash script designed to simplify the process of managing and updating MAC addresses for network interfaces. It provides an easy way to set a specific MAC address, generate random ones, and log changes.

----------

## **Table of Contents**

1.  [Installation](#installation)
2.  [Usage](#usage)
3.  [Features](#features)
6.  [Authors](#authors)
7.  [System Requirements](#system-requirements)

----------

## **Installation**

1.  Clone or download the repository containing `bit_mac.sh`:
    
    ```bash
    git clone https://github.com/WTCSC/mac-address-changer-TAWN05.git
    
    ```
    
2.  Make the script executable:
    
    ```bash
    chmod +x bit_mac.sh
    
    ```
    
3.  Ensure you have the necessary permissions to run network-related commands:
    
    -   The script requires `sudo` for managing network interfaces.

----------

## **Usage**

Run the script using the following syntax:

```bash
./bit_mac.sh <network_interface> <MAC_address/random> [note]

```

### **Arguments**

-   `<network_interface>`: The name of the network interface to update (e.g., `eth0`, `wlan0`).
-   `<MAC_address>`: A specific MAC address to assign, or use `random` to generate a random MAC address.
-   `[note]` (optional): Logs the network interface and MAC address change with a timestamp to `Address_list.txt`.

### **Examples**

1.  Set a specific MAC address:
    
    ```bash
    ./bit_mac.sh eth0 00:11:22:33:44:55
    
    ```
    
2.  Generate and set a random MAC address:
    
    ```bash
    ./bit_mac.sh wlan0 random
    
    ```
    
3.  Generate a random MAC address and log the change:
    
    ```bash
    ./bit_mac.sh eth0 random note
    
    ```
    
4.  View the help message for usage instructions:
    
    ```bash
    ./bit_mac.sh
    
    ```
    

----------

## **Features**

-   **Set Specific MAC Address**: Update your network interface with a specific MAC address.
-   **Random MAC Address Generation**: Automatically generate a random MAC address.
-   **Logging**: Log all changes with timestamps for auditing purposes.
-   **Error Validation**: Ensures MAC address format is valid before applying changes.
-   **User-Friendly**: Displays detailed updates and status messages during execution.

---------

## **Authors**

-   **Primary Developer**: Jacob casey/TAWN05

----------

## **System Requirements**

-   **Operating System**: Linux-based (tested on Ubuntu and similar distributions).
-   **Tools**: `ip` command for managing network interfaces.
-   **Permissions**: Requires `sudo` to modify network settings.
