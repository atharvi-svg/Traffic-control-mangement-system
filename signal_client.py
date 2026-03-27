import socket
import ssl
import time
import json

SERVER_IP = "127.0.0.1"
PORT = 5000

# Define signals
signals = ["Signal_101", "Signal_102", "Signal_103"]

# Each signal has its own cycle
cycles = {
    "Signal_101": ["RED", "YELLOW", "GREEN"],
    "Signal_102": ["YELLOW", "GREEN", "RED"],
    "Signal_103": ["RED", "YELLOW", "GREEN"]
}

# SSL setup
context = ssl._create_unverified_context()

# Create connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_client = context.wrap_socket(client)

secure_client.connect((SERVER_IP, PORT))
print("🚦 Connected to server\n")

while True:
    for signal in signals:
        for state in cycles[signal]:

            # ✅ Send JSON
            message = {
                "signal_id": signal,
                "state": state
            }

            secure_client.send(json.dumps(message).encode())
            print("📤 Sent:", message)

            # ✅ Receive response
            try:
                response = secure_client.recv(1024).decode()
                if response:
                    print("📥 Received:", json.loads(response))
            except Exception as e:
                print("⚠️ Receive error:", e)

            time.sleep(2)

    print("\n------ NEXT ROUND ------\n")