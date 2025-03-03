# P2P Chat System - Team Decryptors

## Team Members

- **Nidarsana M** - Roll no: 230004031 - [GitHub Profile](https://github.com/Nidarsana02)
- **Tripti Anand** - Roll no: 230001078 - [GitHub Profile](https://github.com/Tripti1298) 
- **Nandini Kumari** - Roll no: 230001056 - [GitHub Profile](https://github.com/dini-5002) 

## Contents
- [Overview](#overview)
- [Features](#features)
- [Bonus Question Implementation](#bonus-question-implementation)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [How it works?](#how-it-works)
  - [Running the P2P Chat Application](#running-the-p2p-chat-application)
  - [Mandatory Peers](#mandatory-peers)
  - [Main Menu Options](#main-menu-options)
- [What makes our project unique?](#what-makes-our-project-unique)
- [Code Structure](#code-structure)
- [Sample Workplan (given in assignment)](#sample-workplan-given-in-assignment)
 
## Overview
This is a decentralized Peer-to-Peer (P2P) chat system that allows users to communicate directly without relying on a central server. The system enables multiple peers to connect, send messages, and maintain an active connection network.

## Features
- Peer-to-peer communication without a central server
- Automatic connection to mandatory peers
- Querying of active peers
- Handling of message acknowledgments
- Bonus question has also been attempted
- Effiecient disconnection management
- Peer discovery using UDP broadcasts(rest of the above uses TCP)


## Bonus Question Implementation
The system includes a connect() function that allows peers to establish dynamic connections with active peers after querying. This ensures that newly connected peers are reflected in the active peer list when queried.

## Project Structure
```
|-- main.py       # Main P2P chat application
|-- client.py      # Simple message sender
|-- server.py      # Handles incoming connections and messages
|-- utils.py       # Utility functions for connecting to peers
```

## Requirements
- Python 3.x
- Socket and Threading libraries (built-in)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/p2p-chat.git
   cd p2p-chat
   ```

2. Ensure Python 3 is installed.
3. No additional dependencies are required.

## How it works?

### Running the P2P Chat Application

1. Start the chat application:

   ```sh
   python main.py
   ```

2. Enter your details when prompted:

   - Team name
   - IP Address
   - Port Number
     
Note: Mandatory connect message will be sent to the specified IP address and port number after entering the above mentioned data.

3. Use the menu options to:

    1 - Send messages
    2 - Query active peers
    3 - Connect to known peers
    0 - Quit 


### Mandatory Peers

You can modify the `MANDATORY_PEERS` list in `main.py` to include default peers that should always be connected at startup.

### Main Menu Options
1. **Send message**
   - Input recipient's IP and Port to establish a connection and send messages.
   - Use \`exit\` to disconnect from the recipient.
   - Use \`menu\` to return to the main menu.
   - ![image](https://github.com/user-attachments/assets/cdf38237-4a6e-4975-954b-87f6165a96f8)

2. **Query active peers**
   - Displays peers you've received messages from during the current session(on terminal 2 in picture below).
   - ![image](https://github.com/user-attachments/assets/74b988a7-a7f8-4b7d-8d7d-87f78805989c)

3. **Connect to active peers**
   - Establishes TCP connections to all known active peers.
   - ![image](https://github.com/user-attachments/assets/ac024f22-f210-4498-9ff3-7d44d56055f1)

4. **Previously connected peers**
   - Lists all peers you've connected to in previous sessions (on terminal 3 in the picture below).
   - ![image](https://github.com/user-attachments/assets/de2cbfb6-f17f-43da-b345-9ffd22351a32)

5. **Discover peers**
   - Broadcasts a UDP message to find peers on the network.
   - ![image](https://github.com/user-attachments/assets/fd07e6ba-0964-4bc9-829e-73230e5e5a52)

0. **Quit**
   - Exits the application.
   - ![image](https://github.com/user-attachments/assets/703c0d2e-6560-4451-ae9c-b5cff47a9de6)
     
## What makes our project unique?
Our projects stands out from the rest as

- The query active peers gives the list of active peers, from which it had previously recieved messages from.
- The user can keep sending messages without the need of entering the IP address and port number of the reciever again and again. While sending messages, if we want to return back to use the menu options, "menu" is to be typed and to disconnect from a peer, just type "exit".
- Once a peer is identified through querying, the connect_to_peer() function connects with the peers to initiate communication.
- The query_peers_via_udp() function uses UDP broadcasts to discover available peers on the network, making it simple to find and connect to peers dynamically.
- To disconnect from a peer, press "1" to send message and specify the index of the peer you want to disconnect from and then type "exit".
- "0-Quit" terminates the program.

## Code Structure

- **\`handle_client\`**: Manages incoming TCP connections.
- **\`send_message\`**: Sends messages to connected peers.
- **\`start_server\`**: Initializes the TCP server.
- **\`start_udp_listener\`**: Listens for peer discovery UDP broadcasts.
- **\`query_peers_via_udp\`**: Broadcasts a discovery request to find peers.
- **\`query_peers\`**: Lists currently active peers.
- **\`query_previous_peers\`**: Lists previously connected peers.
- **\`connect_to_peer\`**: Establishes a TCP connection to a peer.
- **\`connect_to_active_peers\`**: Connects to all known active peers.
- **\`send_mandatory_messages\`**: Sends messages to predefined mandatory peers.
- **\`main\`**: Entry point that initializes the server, UDP listener, and user interface.

## Sample Workplan (given in assignment)

![image](https://github.com/user-attachments/assets/7b368a39-5fa5-4d2f-bd08-b23864b31cab)

