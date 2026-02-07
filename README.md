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



### Local Development (Without Docker)

1. **Clone the repository**
   ```bash
   git clone https://github.com/quachphu/CECS327H_Project1.git
   cd CECS327H_Project1
   ```

2. **Run the server**
   ```bash
   python server.py
   ```

3. **Run the client (in a separate terminal)**
   ```bash
   python client.py
   ```

### Docker Deployment 

1. **Clone the repository**
   ```bash
   git clone https://github.com/quachphu/CECS327H_Project1.git
   cd CECS327H_Project1
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **To run in detached mode**
   ```bash
   docker-compose up -d
   ```

4. **To stop the containers**
   ```bash
   docker-compose down
   ```



## References
1. https://docs.python.org/3/library/socket.html
2. https://www.youtube.com/watch?v=esLgiMLbRkI
3. https://www.youtube.com/watch?v=YwWfKitB8aA&t=2213s

---

