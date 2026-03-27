import socket
import ssl
import threading
import json
import time

HOST = "0.0.0.0"
PORT = 5000

# SSL setup
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("🟢 Secure Multi-Client Server Started...\n")

def handle_client(conn, addr):
    print(f"🔗 Connected: {addr}")

    while True:
        try:
            start = time.time()

            data = conn.recv(1024).decode()
            if not data:
                break

            message = json.loads(data)
            print("📥 Received:", message)

            # ✅ Correct traffic light logic
            if message["state"] == "RED":
                next_state = "YELLOW"
            elif message["state"] == "YELLOW":
                next_state = "GREEN"
            else:
                next_state = "RED"

            response = {
                "signal_id": message["signal_id"],
                "action": "CHANGE",
                "next_state": next_state,
                "server_time": time.time()
            }

            conn.send(json.dumps(response).encode())

            latency = time.time() - start
            print(f"⚡ Latency: {latency:.4f} sec\n")

        except Exception as e:
            print("❌ Error:", e)
            break

    conn.close()
    print(f"🔌 Disconnected: {addr}")


while True:
    client_socket, addr = server.accept()
    secure_conn = context.wrap_socket(client_socket, server_side=True)

    thread = threading.Thread(target=handle_client, args=(secure_conn, addr))
    thread.start()