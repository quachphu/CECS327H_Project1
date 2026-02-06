"""
Reference and resources used for this project:
1. https://docs.python.org/3/library/socket.html
2. https://www.youtube.com/watch?v=esLgiMLbRkI
3. https://www.youtube.com/watch?v=YwWfKitB8aA&t=2213s
"""

import socket
from datetime import datetime


def tcp_server():
    """
    Receive messages from clients and send response
    """
    # Create TCP socket
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )  # I learn from this : https://www.youtube.com/watch?v=esLgiMLbRkI
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind socket to host and port (https://www.youtube.com/watch?v=esLgiMLbRkI)
    host = "0.0.0.0"
    port = 5000
    server_socket.bind((host, port))

    # Listen for incoming messages
    server_socket.listen(5)
    print("TCP SERVER STARTED")
    print(f"Listening on {host}:{port}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    connection_count = 0

    try:  # I learn encode, decode from this : https://www.youtube.com/watch?v=esLgiMLbRkI and https://www.youtube.com/watch?v=YwWfKitB8aA&t=2213s
        while True:
            # Accept client connection
            client_socket, client_address = (
                server_socket.accept()
            )  # https://www.youtube.com/watch?v=YwWfKitB8aA&t=2213s
            connection_count += 1

            print(f"\n[Connection #{connection_count}]")
            print(f"Client connected from: {client_address[0]}:{client_address[1]}")

            try:
                data = client_socket.recv(1024).decode("utf-8")

                if data:
                    print(f"Received message: '{data}'")
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    response = f"[SERVER] Message received at {timestamp}: '{data}'"

                    # Sending response back to client
                    client_socket.send(response.encode("utf-8"))
                    print(f"Sent response: '{response}'")
            except Exception as e:
                print(f"Error handling client: {e}")

            finally:
                # Close connection with client
                client_socket.close()

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server socket closed.")


if __name__ == "__main__":
    tcp_server()
