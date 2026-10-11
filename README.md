# SDN-Based Online Examination System

## 1. Project Overview

The SDN-Based Online Examination System is a Python TCP socket application
deployed in a Software-Defined Networking (SDN) environment using Mininet,
Open vSwitch, and the OS-Ken OpenFlow 1.3 controller.

The system allows multiple student clients to connect to a central
examination server through an SDN-controlled virtual network.

## 2. Objectives

- Implement client-server communication using TCP sockets.
- Support concurrent student connections.
- Create a virtual network using Mininet.
- Use an OpenFlow 1.3 controller to manage switch forwarding.
- Test connectivity between network hosts.
- Inspect forwarding rules installed on the virtual switch.
- Demonstrate communication between student clients and the examination server.

## 3. Technologies Used

- Python 3
- TCP sockets
- Mininet
- Open vSwitch
- OS-Ken SDN controller
- OpenFlow 1.3
- Ubuntu Linux

## 4. Network Architecture

The topology consists of four hosts connected to one OpenFlow switch.
The switch communicates with the OS-Ken controller.

| Component | Role | IP Address |
|-----------|------|------------|
| h1 | Student 1 | 10.0.0.1 |
| h2 | Student 2 | 10.0.0.2 |
| h3 | Student 3 | 10.0.0.3 |
| h4 | Examination Server | 10.0.0.4 |
| s1 | OpenFlow Switch | N/A |
| c0 | SDN Controller | 127.0.0.1:6653 |

The examination server listens on TCP port 5000.
Student clients connect to 10.0.0.4:5000.

The controller implements an OpenFlow 1.3 learning switch.
It learns source MAC addresses, forwards packets to known destinations,
and floods packets when the destination is unknown.
It also installs forwarding rules for known destinations.

## 5. Project Structure

online-examination-sdn/
├── application/
│   ├── server.py
│   └── client.py
├── controller/
│   └── controller.py
├── mininet/
│   └── topology.py
├── controller-env/
└── README.md

## 6. Setup Requirements

The environment requires:

- Ubuntu Linux
- Python 3
- Mininet
- Open vSwitch
- An installed OS-Ken controller
- The Python virtual environment named controller-env

## 7. How to Run the Project

### Step 1: Start the SDN Controller

Open a terminal and run:

    cd ~/online-examination-sdn
    source controller-env/bin/activate
    osken-manager --ofp-tcp-listen-port 6653 --verbose controller/controller.py

Keep the controller terminal open.

### Step 2: Start the Mininet Network

Open a second terminal and run:

    cd ~/online-examination-sdn
    sudo python3 mininet/topology.py

Wait for the Mininet prompt:

    mininet>

### Step 3: Test Network Connectivity

At the Mininet prompt, run:

    pingall

All four hosts should be able to communicate.

### Step 4: Start the Examination Server

At the Mininet prompt, run:

    h4 python3 /home/shahid-os/online-examination-sdn/application/server.py &

Check that the server is listening:

    h4 ss -ltnp | grep 5000

### Step 5: Launch Student Clients

At the Mininet prompt, run:

    xterm h1 h2 h3

In each student terminal, execute:

    python3 /home/shahid-os/online-examination-sdn/application/client.py

Each client connects to the examination server at 10.0.0.4:5000.

Students can receive questions, submit answers, and view their scores.

### Step 6: Inspect OpenFlow Rules

At the Mininet prompt, run:

    sh ovs-ofctl -O OpenFlow13 dump-flows s1

The output displays the rules installed on the switch, including
the default controller rule and learned forwarding rules.

## 8. Testing and Results

### Test 1: Network Connectivity

Command:

    pingall

Observed result:

    0% packet loss (12/12 packets received)

Result: Successful communication between the four Mininet hosts.

### Test 2: TCP Examination Application

A student client connected to the examination server, received
questions, submitted answers, and received a final score.

Result: The examination session completed successfully.

### Test 3: Concurrent Student Connections

Two student clients were started simultaneously and completed their
examinations.

Both clients received their results.

Result: Concurrent TCP client handling was demonstrated successfully.

### Test 4: SDN Controller Connectivity

The OS-Ken controller successfully connected to the OpenFlow 1.3 switch.

The controller received packet-in events and learned source MAC addresses.

Result: The controller communicated with the switch and processed traffic.

### Test 5: Forwarding Rule Installation

The switch flow table displayed forwarding rules for traffic between hosts.

The observed rules used priority 1 and forwarded packets to the appropriate
switch ports.

Result: Controller-driven forwarding rule installation was verified.

## 9. Future Enhancements

- Dynamic traffic monitoring and traffic-aware forwarding.
- Examination time limits and session management.
- More extensive simultaneous-client testing.
- Performance measurements under different traffic conditions.
- Comparison of controller-managed forwarding and standalone switching.
- Automated testing and improved result reporting.

## 10. Conclusion

The project integrates Python TCP socket programming with a Mininet
network controlled using OS-Ken and OpenFlow 1.3.

Initial testing demonstrated successful host connectivity, controller
communication, MAC learning, forwarding rule installation, and examination
sessions involving multiple student clients.

The project provides a foundation for additional SDN functionality
and performance evaluation in the next development phase.
