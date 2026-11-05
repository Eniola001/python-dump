# import socket

# # Hostnames to test
# hosts = ["www.google.com", "gaia.cs.umass.edu"]

# for host in hosts:
#     print("\n" + "=" * 60)
#     print("Hostname:", host)

#     try:
#         # Resolve the hostname to an IP address
#         ip_address = socket.gethostbyname(host)
#         print("IP Address:", ip_address)

#         # Create a TCP socket and connect to the web server
#         client_socket = socket.socket(
#             socket.AF_INET,
#             socket.SOCK_STREAM
#         )

#         client_socket.settimeout(10)
#         client_socket.connect((host, 80))

#         # Construct the HTTP request
#         request = (
#             f"GET / HTTP/1.1\r\n"
#             f"Host: {host}\r\n"
#             f"Connection: close\r\n"
#             f"\r\n"
#         )

#         # Send the request
#         client_socket.sendall(request.encode("ascii"))

#         # Receive and print the HTTP response
#         response = b""

#         while True:
#             data = client_socket.recv(4096)

#             if not data:
#                 break

#             response += data

#         print("\nHTTP Response:")
#         print(response.decode("utf-8", errors="replace"))

#         client_socket.close()

#     except socket.timeout:
#         print("Error: Connection timed out.")

#     except socket.gaierror:
#         print("Error: Could not resolve hostname.")

#     except OSError as error:
#         print("Network error:", error)

# BONUS
import socket
import ssl

# Hostnames to test
hosts = ["www.google.com", "gaia.cs.umass.edu"]

for host in hosts:
    print("\n" + "=" * 60)
    print("Hostname:", host)

    try:
        # Resolve the hostname
        ip_address = socket.gethostbyname(host)
        print("IP Address:", ip_address)

        # Create a default TLS context
        context = ssl.create_default_context()

        # Establish a TCP connection and wrap it with TLS
        with socket.create_connection(
            (host, 443),
            timeout=10
        ) as raw_socket:

            with context.wrap_socket(
                raw_socket,
                server_hostname=host
            ) as secure_socket:

                # Construct the HTTPS request
                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"Connection: close\r\n"
                    f"\r\n"
                )

                # Send the request
                secure_socket.sendall(
                    request.encode("ascii")
                )

                # Receive the response
                response = b""

                while True:
                    data = secure_socket.recv(4096)

                    if not data:
                        break

                    response += data

                print("\nHTTPS Response:")
                print(
                    response.decode(
                        "utf-8",
                        errors="replace"
                    )
                )

    except socket.timeout:
        print("Error: Connection timed out.")

    except socket.gaierror:
        print("Error: Could not resolve hostname.")

    except ssl.SSLError as error:
        print("SSL/TLS error:", error)

    except OSError as error:
        print("Network error:", error)

# Questions and Answers

# 1. What is a port?

# A port is a logical communication endpoint used by a computer to direct network traffic to the appropriate application or service.

# An IP address identifies a network interface, while a port number helps identify the service receiving the traffic.

# Port numbers range from 0 to 65535.

# For example:

#     Port 80 is commonly used for HTTP.
#     Port 443 is commonly used for HTTPS.
#     Port 22 is commonly used for SSH.

# A computer can run multiple network services using the same IP address, provided they use different ports where required.


# 2. What are the ports for HTTP and HTTPS?

# The standard port numbers are:
# Protocol	Default port	Purpose
# HTTP	        80	        Transfers web requests and responses without transport-layer encryption.
# HTTPS	       443	        Transfers web requests and responses over TLS-encrypted connections.

# These are the default ports, although a server can be configured to use other ports.

# For example, an HTTP URL such as http://example.com normally uses port 80, while https://example.com normally uses port 443.


# 3. What is a socket in networking?

# A socket is a software endpoint that allows a program to send and receive data over a network.

# In Python, the socket module provides an interface for creating and managing network connections.

# A socket can be used for communication through protocols such as TCP and UDP.

# 4. Why is HTTP unsafe?

# HTTP is considered unsafe for transmitting sensitive information because it does not encrypt communication by itself.

# The main security risks are:

#     Lack of encryption: Data travels in plaintext and may be readable by someone who can intercept the traffic.
#     Eavesdropping: Attackers on an exposed or compromised network may be able to read transmitted information.
#     Data modification: An attacker who can intercept the connection may alter requests or responses.
#     Lack of server authentication: HTTP alone does not provide TLS certificate-based authentication of the server.

# For example, if a website sends login credentials over ordinary HTTP, someone who can capture the traffic may be able to read those credentials.
# Why is HTTPS safer?

# HTTPS uses TLS to protect communication between a client and a server.

# It provides three important security properties:

#     Confidentiality: Encryption helps prevent unauthorized parties from reading transmitted data.
#     Integrity: TLS helps detect unauthorized modification of data in transit.
#     Authentication: Certificate validation helps the client verify the server's identity.

# HTTPS is therefore the preferred protocol for websites, especially those handling passwords, personal information, and payment details.

# However, HTTPS does not guarantee that a website is trustworthy or free from malicious content. It protects the connection, not the overall intentions of the website.