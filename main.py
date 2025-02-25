#       DECRYPTORS
# Nidarsana M - 230004031
# Tripti Anand - 230001078
# Nandini Kumari -  230001056

import socket
import threading

active_peers = {}  # Maps peer IP to their listening port
received_from = {}  # Tracks peers from whom messages were received
active_connections = {}  # Stores active socket connections
previous_peers = {}  # Stores previously connected peers with team names

MANDATORY_PEERS = [
    ("10.206.5.228", 6555)
]

UDP_PORT = 50000  # Port for peer discovery broadcasts


def handle_client(client_socket, client_address):
    """
    This function is designed to handle a client connection with a specified socket and address.

    :param client_socket: A client socket object representing the connection to the client

    :param client_address: The `client_address` parameter typically refers to the address of the client
    connecting to the server. 
    """
    try:
        sender_port_data = client_socket.recv(1024).decode().strip()
        data_parts = sender_port_data.split("\n", 2)

        try:
            sender_port = int(data_parts[0]) if data_parts[0].isdigit() else None
        except ValueError:
            sender_port = None

        team_name = data_parts[1] if len(data_parts) > 1 else "Unknown"

        if sender_port:
            active_peers[client_address[0]] = sender_port
            previous_peers[(client_address[0], sender_port)] = team_name
            if client_address[0] not in received_from:
                received_from[client_address[0]] = set()
            received_from[client_address[0]].add(sender_port)
            print(f"🔵 Connected to {client_address[0]}:{sender_port} ({team_name})")

            if len(data_parts) > 2:
                message = data_parts[2].strip()
                print(f"📩 Received from {client_address[0]}:{sender_port}: {message}")
                client_socket.sendall(f"✅ Message received successfully!".encode())

        else:
            print(f"⚠️ Invalid sender port received from {client_address[0]}: {sender_port_data}")
            return

        while True:
            message = client_socket.recv(1024).decode().strip()
            """
            receives data from the client socket connection, decoding it from bytes to a string
            using UTF-8 encoding, and then stripping any leading or trailing whitespaces from the
            received message.
            """
            
            if not message:
                continue

            if message.lower() == "exit":
                print(f"🔴 Client {client_address[0]}:{sender_port} disconnected.")
                active_connections.pop((client_address[0], sender_port), None)
                received_from.get(client_address[0], set()).discard(sender_port)
                break

            received_from[client_address[0]].add(sender_port)
            print(f"📩 Received from {client_address[0]}:{sender_port}: {message}")
            client_socket.sendall(f"✅ Your message was succesfully received!".encode())

    except Exception as e:
        print(f"⚠️ Connection error with {client_address[0]}: {e}")
    finally:
        client_socket.close()
        received_from.get(client_address[0], set()).discard(sender_port)
        active_connections.pop((client_address[0], sender_port), None)


def send_message(ip, port, my_port, team_name):
    """
    This function sends a message to a specified IP address and port, using a specific port.

    :param ip: The `ip` parameter is the IP address of the destination server

    :param port:  port number of the destination server or

    :param my_port: The `my_port` parameter is the port number used to send the message. 
    """
    if (ip, port) not in active_connections:
        connect_to_peer(ip, port, my_port, team_name)

    if (ip, port) in active_connections:
        conn = active_connections[(ip, port)]
        while True:
            message = input("Enter message (type 'exit' to disconnect, 'menu' for options): ").strip()
            if message.lower() == 'menu':
                break
            elif message.lower() == "exit":
                conn.sendall("exit\n".encode())
                conn.close()
                active_connections.pop((ip, port), None)
                print(f"🔴 Disconnected from {ip}:{port}")
                break
            try:
                conn.sendall(f"{message}\n".encode())
                ack = conn.recv(1024).decode().strip()
                print(f"✅ Acknowledgment from {ip}:{port} - {ack}")
            except Exception as e:
                print(f"❌ Error sending message to {ip}:{port} - {e}")
                conn.close()
                active_connections.pop((ip, port), None)
                break
    else:
        print(f"❌ Not connected to {ip}:{port}")


def start_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow address reuse
    server_socket.bind((ip, port))
    server_socket.listen(5)

    print(f"Server listening on {ip}:{port}...")
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()



def start_udp_listener(my_port, team_name):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(("", UDP_PORT))

    print(f"🔎 Listening for peer discovery on UDP port {UDP_PORT}...")
    while True:
        data, addr = udp_socket.recvfrom(1024)
        message = data.decode().strip()
        if message == "Who is online?":
            response = f"{my_port}\n{team_name}"
            udp_socket.sendto(response.encode(), addr)
            print(f"📡 Responded to discovery request from {addr[0]}:{addr[1]}")


def query_peers_via_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_socket.settimeout(3)

    message = "Who is online?"
    udp_socket.sendto(message.encode(), ('<broadcast>', UDP_PORT))

    print("\nDiscovered Peers 📡:")
    try:
        while True:
            data, addr = udp_socket.recvfrom(1024)
            response = data.decode().strip().split("\n")
            peer_port = response[0]
            peer_team = response[1] if len(response) > 1 else "Unknown"
            print(f"{addr[0]}:{peer_port} - Team: {peer_team}")
    except socket.timeout:
        print("🔎 Above is the list of peers who are online.")


def query_peers():
    print("\nConnected Peers:")
    active = False
    for peer_ip, ports in received_from.items():
        for port in ports:
            print(f"{peer_ip}:{port} - Active")
            active = True

    if not active:
        print("No connected peers 😔")


def query_previous_peers():
    print("\nPreviously Connected Peers:")
    if not previous_peers:
        print("😔 You have not been previously connected with any peers.")
    else:
        for (ip, port), team in previous_peers.items():
            print(f"{ip}:{port} - Team: {team}")


def connect_to_peer(ip, port, my_port, team_name):
    try:

        if (ip, port) not in active_connections:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, port))
            client_socket.sendall(f"{my_port}\n{team_name}\nCONNECT\n".encode())
            active_connections[(ip, port)] = client_socket
            print(f"✅ Successfully connected to {ip}:{port}:{team_name}")
        else:
            print(f"Already connected to {ip}:{port}:{team_name}")
    except Exception as e:
        print(f"❌ Error connecting to {ip}:{port} - {e}")


def connect_to_active_peers(my_port, team_name):
    for peer_ip, ports in received_from.items():
        for port in ports:
            if (peer_ip, port) not in active_connections:
                connect_to_peer(peer_ip, port, my_port, team_name)

def send_mandatory_messages(my_port, team_name):
    for ip, port in MANDATORY_PEERS:
        try:
            connect_to_peer(ip, port, my_port, team_name)
            if (ip, port) in active_connections:
                conn = active_connections[(ip, port)]
                conn.sendall(f"Decryptors here!\n".encode())
                print(f"✅ Hurray! Mandatory message sent to {ip}:{port}")
        except Exception as e:
            print(f"❌ Could not send mandatory message to {ip}:{port} - {e}")


def main():
    print("DECRYPTORS - P2P Chat Application")
    team_name = input("Enter your team name: ")
    ip = input("Enter your IP address: ")
    port = int(input("Enter your port number: "))
    print(f"Hello, {team_name}")

    # Start TCP server for chat
    server_thread = threading.Thread(target=start_server, args=(ip, port))
    server_thread.daemon = True
    server_thread.start()

    # Start UDP listener for peer discovery
    udp_listener_thread = threading.Thread(target=start_udp_listener, args=(port, team_name))
    udp_listener_thread.daemon = True
    udp_listener_thread.start()

    send_mandatory_messages(port, team_name)

    while True:
        print("\n***** Menu *****")
        print("1. Send message")
        print("2. Query active peers")
        print("3. Connect to active peers")
        print("4. Previously connected peers")
        print("5. Discover peers: Who is online?")
        print("0. Quit")

        choice = input("Enter choice: ")
        if choice == "1":
            recipient_ip = input("Enter recipient's IP: ")
            recipient_port = int(input("Enter recipient's Port: "))
            send_message(recipient_ip, recipient_port, port, team_name)
        elif choice == "2":
            query_peers()
        elif choice == "3":
            connect_to_active_peers(port, team_name)
        elif choice == "4":
            query_previous_peers()
        elif choice == "5":
            query_peers_via_udp()
        elif choice == "0":
            print("Hope you had a good chat with peers on the network. Meet you again!")
            break


if __name__ == "__main__":
    main()