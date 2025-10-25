# Simple Messenger App

A classic, simple messenger application built with Python using TCP sockets. Multiple clients can connect to a central server and chat together in real-time.

## Features

- Multi-client support (multiple users can chat simultaneously)
- Real-time messaging
- Username identification
- Join/leave notifications
- Pure Python implementation using standard library

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## How to Run

### Step 1: Start the Server

First, open a terminal/command prompt and run the server:

```bash
python server.py
```

You should see:
```
Server is running on 127.0.0.1:5555
Waiting for connections...
```

### Step 2: Connect Clients

Open additional terminal windows (one for each user) and run the client:

```bash
python client.py
```

When prompted, enter a username:
```
Enter your username: Alice
```

You can open multiple client terminals to simulate multiple users chatting.

### Step 3: Start Chatting!

Once connected, simply type your message and press Enter to send it to all connected users.

## Example Usage

**Server Terminal:**
```
Server is running on 127.0.0.1:5555
Waiting for connections...
Connected with ('127.0.0.1', 54321)
Username: Alice
Connected with ('127.0.0.1', 54322)
Username: Bob
```

**Client 1 (Alice):**
```
Enter your username: Alice
Connected to the server!
Alice has joined the chat!
Bob has joined the chat!
Hello everyone!
Alice: Hello everyone!
Bob: Hi Alice!
```

**Client 2 (Bob):**
```
Enter your username: Bob
Connected to the server!
Bob has joined the chat!
Alice: Hello everyone!
Hi Alice!
Bob: Hi Alice!
```

## Architecture

- **server.py**: TCP server that accepts multiple client connections and broadcasts messages to all connected clients
- **client.py**: TCP client that connects to the server and handles sending/receiving messages
- Uses threading to handle multiple simultaneous connections
- Messages are encoded/decoded using UTF-8

## Configuration

To change the server address or port, edit the following variables in both `server.py` and `client.py`:

```python
HOST = '127.0.0.1'  # Server IP address
PORT = 5555         # Server port
```

**Note:** If you want to chat across different computers on the same network, change `HOST` to the server's local IP address (e.g., `192.168.1.x`).

## Stopping the Application

- To disconnect a client: Press `Ctrl+C` in the client terminal
- To stop the server: Press `Ctrl+C` in the server terminal

## Limitations

This is a basic implementation for learning purposes. It does not include:
- Message encryption
- User authentication
- Message history/persistence
- Private messaging
- GUI interface

## License

Free to use and modify for educational purposes.

