import socket


def start_server(host='127.0.0.1', port=65432):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Bind the socket to the port
            server_socket.bind((host, port))
            print(f"Server started on {host}:{port}")

            # Listen for incoming connections
            server_socket.listen()
            print("Waiting for connection...")

            # Accept connection
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                # Send message to client
                conn.sendall(b"Hello from server!")

    except Exception as e:
        print(f"Server error: {e}")


if __name__ == "__main__":
    start_server()