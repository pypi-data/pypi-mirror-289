import socket
import struct

def execute(script):
    header = bytearray(16)
    struct.pack_into('<I', header, 8, len(script) + 1)

    try:
        with socket.create_connection(('127.0.0.1', 5553), timeout=3) as s:
            s.sendall(header + script.encode() + b'\x00')
            print('F9 in Roblox to see script activity.')
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
