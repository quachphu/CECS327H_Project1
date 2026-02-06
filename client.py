"""
Reference and resources used for this project:
1. https://docs.python.org/3/library/socket.html
2. https://www.youtube.com/watch?v=esLgiMLbRkI
3. https://www.youtube.com/watch?v=YwWfKitB8aA&t=2213s
"""

import socket
import time
import os
from datetime import datetime


def tcp_client():
    """
    TCP client connects to server, sends message, and receives response
    """
    # Get information from environment variables
    server_host = os.getenv("SERVER_HOST", "server")
    server_port = int(os.getenv("SERVER_PORT", "5000"))
    client_name = os.getenv("CLIENT_NAME", "Unknown Client")

    print(f"TCP CLIENT: {client_name}")
    print(f"Connecting server at {server_host}:{server_port}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    time.sleep(2)

    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:  # Encode and Decode I learn from this : https://www.youtube.com/watch?v=esLgiMLbRkI and https://www.youtube.com/watch?v=YwWfKitB8aA&t=2213s
        # Connect to server
        print(f"\nConnecting to {server_host}:{server_port}...")
        client_socket.connect((server_host, server_port))
        print(" Connected successfully!")

        # Create message
        timestamp = datetime.now().strftime("%H:%M:%S")
        message = f"Hello from {client_name} at {timestamp}"

        # Send message to server
        print(f"\nSending: '{message}'")
        client_socket.send(message.encode("utf-8"))

        # Receive response from server
        response = client_socket.recv(1024).decode("utf-8")
        print(f"Received: '{response}'")

        print("Client Finished Communication")

    except ConnectionRefusedError:
        print(f"\nCannot connect to server at {server_host}:{server_port}")
    except Exception as e:
        print(f"\nERROR: {e}")
    finally:
        client_socket.close()
        print("\nClient socket closed.")


if __name__ == "__main__":
    tcp_client()
