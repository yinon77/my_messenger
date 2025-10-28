"""
Simple Messenger Client
A basic TCP client that connects to the messenger server and allows sending/receiving messages.
NEW FEATURES:
- Timestamps on all messages
- Chat history when you join
- Emoji support (just type emojis normally! 😊)
"""

import socket
import threading
from datetime import datetime  # For message timestamps

# Server configuration - must match server settings
HOST = '127.0.0.1'  # Server address (localhost)
PORT = 5555         # Server port

# Get username from user
print("=" * 50)
print("Welcome to Simple Messenger! 💬")
print("You can use emojis in your messages! 😊👍🎉")
print("=" * 50)
username = input("Enter your username: ")

# Create client socket and connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive_messages():
    """
    Continuously listen for incoming messages from the server
    Runs in a separate thread
    """
    while True:
        try:
            # Receive message from server
            message = client.recv(1024).decode('utf-8')
            
            # If server requests username, send it
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                # Display the message
                print(message)
        except:
            # If error occurs, close connection and break
            print('An error occurred!')
            client.close()
            break


def send_messages():
    """
    Continuously send messages typed by the user to the server
    Runs in the main thread
    """
    while True:
        try:
            # Get message from user
            message = input('')
            
            # NEW FEATURE: Add timestamp to message
            timestamp = datetime.now().strftime('%H:%M:%S')
            
            # Format message with timestamp, username, and send to server
            # Emojis work automatically with UTF-8 encoding! 😊
            full_message = f'[{timestamp}] {username}: {message}'
            client.send(full_message.encode('utf-8'))
        except:
            # If error occurs, close connection and break
            print('An error occurred!')
            client.close()
            break


# Start thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start sending messages (runs in main thread)
send_messages()
