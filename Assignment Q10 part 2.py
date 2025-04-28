import socket


def connect_to_server(host='127.0.0.1', port=65432):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to server
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")

            # Receive data from server
            data = client_socket.recv(1024)
            print(f"Received message: {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print("Error: Could not connect to server")
    except Exception as e:
        print(f"Client error: {e}")


if connect_to_server == "_main_":
    connect_to_server()