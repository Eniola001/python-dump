import socket

# Get the host name of the computer
hostname = socket.gethostname()

# Get the local IP address
local_ip = socket.gethostbyname(hostname)

# Print the results
print("Host Name:", hostname)
print("Local IP Address:", local_ip)


# Questions and Answers

# 1. Who decided what your host name was?

# The host name was generally chosen when the computer's operating system was installed or configured. It may have been assigned by:

#     The computer manufacturer.
#     The user who set up the computer.
#     A system administrator in an organization.
#     An organization’s network management system.

# For example, a computer might have the host name DESKTOP-ABC123.

# 2. Who decided what your local IP address was?

# The local IP address is usually assigned by the network's DHCP (Dynamic Host Configuration Protocol) server, commonly running on a home router.

# Alternatively:

#     A user or system administrator can configure a static IP address manually.
#     An organization’s network administrator can assign addresses according to its network configuration.

# For example, 192.168.1.5 is a private IP address commonly used on local networks.

# 3. What is the host name and/or local IP address used for?

# The host name and local IP address help identify and communicate with a computer on a network.

#     Host name: Provides a human-readable name for a computer, making it easier to identify than a numerical IP address.
#     Local IP address: Identifies a network interface on a local network so devices can communicate with it.

# For example, a computer can use an IP address to communicate with a printer or another computer on the same network.

# Host names can also be used for network administration and troubleshooting. IP addresses help route network traffic to the appropriate destination.