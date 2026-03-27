# Smart Signal Monitoring System (SSMS)
## Karnataka State Police – Traffic Division
### PES University, CN Project

---

## Project Structure
```
smart-signal/
├── server/
│   ├── server.py          ← Central monitoring server (Flask + WebSocket)
│   ├── signal_client.py   ← Signal unit client simulator
│   └── requirements.txt   ← Python dependencies
└── client/
    └── index.html         ← Full monitoring dashboard (open in browser)
```

---

## Quick Start

### 1. Install Server Dependencies
```bash
cd server
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python server.py
```
Server runs on: `http://0.0.0.0:5000`

### 3. Open the Dashboard
- Open `client/index.html` in any browser
- Change `SERVER_URL` in the JS to your server IP if on a different machine:
  ```js
  const SERVER_URL = 'http://<server-ip>:5000';
  const DEMO_MODE = false;  // Set to false for live server
  ```

### 4. (Optional) Run Signal Client Simulator
```bash
python signal_client.py --id SIG-TEST --name "Test Junction" --server http://localhost:5000
```

---

## Features

| Feature | Description |
|---|---|
| Real-time WebSocket updates | Signal states pushed every 2 seconds |
| Traffic light visual | Animated R/Y/G display per signal |
| Operator override | Force any signal to RED/YELLOW/GREEN |
| Fault detection | Auto-detects lamp failure, sensor errors, etc. |
| Fault log | Live log with resolved/active status |
| Vehicle count | Per-junction count with bar chart |
| Performance metrics | Latency, uptime, packet count, clients |
| Alert banner | Scrolling alert for active faults |
| Demo mode | Works offline without a server |

---

## REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/signals` | All signal states |
| GET | `/api/signals/<id>` | Single signal state |
| POST | `/api/signals/<id>/override` | Override phase |
| POST | `/api/signals/<id>/reset` | Reset faulted signal |
| GET | `/api/faults` | Fault log |
| GET | `/api/metrics` | Server performance metrics |
| GET | `/api/health` | Health check |

---

## Architecture
```
[Signal Units] ──WebSocket──► [Central Server (Flask)]
                                      │
                              REST API + WebSocket
                                      │
                              [Dashboard Client]
                              (Browser / Remote PC)
```

---

## Tech Stack
- **Server**: Python, Flask, Flask-SocketIO, Flask-CORS
- **Client**: HTML5, CSS3, Vanilla JS, Chart.js, Socket.IO
- **Protocol**: WebSocket (real-time), HTTP REST (on-demand)
- **Networking**: Client–Server Architecture (CN Project concept)

---

*Done by: Atharvi Desurkar, Chandana Rani S, Aarati Panchal – PES University*
