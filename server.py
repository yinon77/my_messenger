"""
Simple Messenger Server
A basic TCP socket server that allows multiple clients to connect and chat together.
"""

import socket
import threading
from datetime import datetime  # For message timestamps

# Server configuration
HOST = '127.0.0.1'  # Localhost - server runs on local machine
PORT = 5555         # Port to listen on

# List to keep track of all connected clients
clients = []
# List to keep track of client usernames
usernames = []

# NEW FEATURE: Chat history
# Stores all messages sent in the chat session
chat_history = []


def broadcast(message, save_to_history=True):
    """
    Send a message to all connected clients
    
    Args:
        message (bytes): The message to broadcast to all clients
        save_to_history (bool): Whether to save this message to chat history
    """
    # NEW FEATURE: Save message to chat history
    if save_to_history:
        # Get current timestamp
        timestamp = datetime.now().strftime('%H:%M:%S')
        # Decode message and store with timestamp
        message_text = message.decode('utf-8')
        chat_history.append(f'[{timestamp}] {message_text}')
        print(f'[{timestamp}] {message_text}')  # Also display on server
    
    for client in clients:
        try:
            client.send(message)
        except:
            # If sending fails, remove the client
            remove_client(client)


def remove_client(client):
    """
    Remove a client from the server when they disconnect
    
    Args:
        client (socket): The client socket to remove
    """
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        username = usernames[index]
        usernames.remove(username)
        broadcast(f'{username} has left the chat!'.encode('utf-8'))
        print(f'{username} disconnected.')


def handle_client(client):
    """
    Handle incoming messages from a specific client
    
    Args:
        client (socket): The client socket to handle
    """
    while True:
        try:
            # Receive message from client
            message = client.recv(1024)
            if message:
                # Broadcast the message to all clients
                broadcast(message)
            else:
                # Empty message means client disconnected
                remove_client(client)
                break
        except:
            # If error occurs, remove the client
            remove_client(client)
            break


def receive_connections():
    """
    Main server loop - accepts new client connections
    """
    print(f'Server is running on {HOST}:{PORT}')
    print('Waiting for connections...')
    print('📨 Emoji support enabled! 😊')  # NEW FEATURE: Emoji support demo
    
    while True:
        # Accept new connection
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        
        # Request username from client
        client.send('USERNAME'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        
        # Add client to lists
        clients.append(client)
        usernames.append(username)
        
        # Announce new user to everyone
        print(f'Username: {username}')
        broadcast(f'{username} has joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))
        
        # NEW FEATURE: Send chat history to new client
        if chat_history:
            client.send('\n--- Chat History ---'.encode('utf-8'))
            for old_message in chat_history:
                client.send(old_message.encode('utf-8'))
            client.send('--- End of History ---\n'.encode('utf-8'))
        
        # Start a new thread to handle this client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Start accepting connections
receive_connections()
