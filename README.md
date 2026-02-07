# CECS327H Project 1 - TCP Socket Programming

## Overview
This project implements a TCP client-server application using Python sockets, demonstrating fundamental concepts of network programming and distributed systems.


## Project Structure
```
CECS327H_Project1/
├── server.py              # TCP server implementation
├── client.py              # TCP client implementation
├── app.py                 # Alternative application entry point
├── index.html             # Web interface (if applicable)
├── Dockerfile             # Base Docker configuration
├── Dockerfile.server      # Server-specific Docker configuration
├── Dockerfile.client      # Client-specific Docker configuration
├── docker-compose.yml     # Multi-container orchestration
└── README.md              
```

## Installation & Setup

### 1. Install Docker

```bash
# Download Docker Desktop from https://www.docker.com/products/docker-desktop
# Install and start Docker Desktop
```

**Verify installation:**
```bash
docker --version
docker run hello-world
```

### 2. Clone Repository
```bash
git clone https://github.com/quachphu/CECS327H_Project1.git
cd CECS327H_Project1
```

---

## How to Run

### Task 0: Basic Python Container

**Build the image:**
```bash
docker build -t my-python-app .
```

**Run the container:**
```bash
docker run my-python-app
```

**Expected output:**
```
Hello, Docker! This is my first containerized app.
Created by: Phu Thien Quach and Luis Reyes
CECS 327 - Networks & Distributed Computing
```

---

### Task 1: Nginx Web Server

**Step 1: Pull Nginx image**
```bash
docker pull nginx:latest
```

**Step 2: Run basic Nginx (default page)**
```bash
docker run -d -p 8080:80 --name my-nginx nginx:latest
```

Visit: `http://localhost:8080` to see Nginx welcome page.

**Step 3: Run Nginx with custom HTML**
```bash
# Stop and remove previous container
docker stop my-nginx
docker rm my-nginx

# Run with volume mount
docker run -d -p 8080:80 \
  -v $(pwd)/index.html:/usr/share/nginx/html/index.html \
  --name my-custom-nginx \
  nginx:latest
```

Visit: `http://localhost:8080` to see custom page.

**Clean up:**
```bash
docker stop my-custom-nginx
docker rm my-custom-nginx
```

---

### Task 2: Multi-Container Setup (Server + Clients)

This task demonstrates container communication using Docker Compose.

**Architecture:**
- 1 TCP Server (listening on port 5000)
- 3 TCP Clients (sending messages to server)
- Custom Docker network for inter-container communication

**Build all images:**
```bash
docker-compose build
```

**Run all containers:**
```bash
docker-compose up
```

**Expected output:**
```
tcp-server    | TCP SERVER STARTED
tcp-server    | Listening on 0.0.0.0:5000
tcp-client-1  | Connecting to server:5000...
tcp-client-1  | ✓ Connected successfully!
tcp-client-1  | Sending: 'Hello from Client-1 (Phu) at XX:XX:XX'
tcp-server    | [Connection #1]
tcp-server    | Received message: 'Hello from Client-1 (Phu) at XX:XX:XX'
tcp-client-1  | Received: '[SERVER] Message received at XX:XX:XX: ...'
[Similar logs for client-2 and client-3]
```

**View logs (in separate terminal):**
```bash
# All logs
docker-compose logs

# Server logs only
docker logs tcp-server

# Specific client logs
docker logs tcp-client-1
```

**Stop all containers:**
```bash
docker-compose down
```

---





## References
1. https://docs.python.org/3/library/socket.html
2. https://www.youtube.com/watch?v=esLgiMLbRkI
3. https://www.youtube.com/watch?v=YwWfKitB8aA&t=2213s

---

