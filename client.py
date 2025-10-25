"""
Simple Messenger Client
A basic TCP client that connects to the messenger server and allows sending/receiving messages.
"""

import socket
import threading

# Server configuration - must match server settings
HOST = '127.0.0.1'  # Server address (localhost)
PORT = 5555         # Server port

# Get username from user
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
            
            # Format message with username and send to server
            full_message = f'{username}: {message}'
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

