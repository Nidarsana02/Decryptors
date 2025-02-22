# P2P Chat System - Team Decryptors

## Overview
This is a decentralized Peer-to-Peer (P2P) chat system that allows users to communicate directly without relying on a central server. The system enables multiple peers to connect, send messages, and maintain an active connection network.

## Features
- Peer-to-peer communication without a central server
- Automatic connection to mandatory peers
- Querying of active peers
- Handling of message acknowledgments
- Bonus question has also been attempted
- Effiecient disconnection management

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

## Usage/ Procedure

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

You can modify the `MANDATORY_PEERS` list in `final.py` to include default peers that should always be connected at startup.


## What makes our project unique?
Our projects stands out from the rest as

- The query active peers not only gives the list of active peers, but it also includes the inactive peers to see the history of all the peers who were connected.
- When, "1-Send messages" is chosen, there appears an additional option to choose whether
       a. to send messages to already connected peers, or
       b. send to a new peer.
     When "a." is chosen, the list of connected peers appear to choose from for the receipient and we can select the index of the peer that we want.
     When "b." is chosen, user is prompted to enter the IP address and the port of the new peer to be connected to.
- The user can keep sending messages without the need of entering the IP address and port number of the reciever again and again. While sending messages, if we want to return back to use the menu options, "menu" 
  is to be typed and to disconnect from a peer, just type "exit".
- Once a peer is identified through querying, the connect_to_peer() function connects with the peers to initiate communication.
- To disconnect from a peer, press "1" to send message and specify the index of the peer you want to disconnect from and then type "exit".
- "0-Quit" terminates the program.



## Team Members

- **Nidarsana M** - [GitHub Profile](https://github.com/Nidarsana02) - Roll no: 230004031
- **Tripti Anand** - [GitHub Profile](https://github.com/Tripti1298) - Roll no: 230001078
- **Nandini Kumari** - [GitHub Profile](https://github.com/dini-5002) - Roll no: 230001056
