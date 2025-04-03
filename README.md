# Advanced Computer Networks CTF Project
## Project Overview
This project is a **Capture The Flag (CTF)** challenge created as part of an advanced computer networks course.
The challenge consists of five stages, each requiring different cybersecurity skills, including network analysis, cryptography, and ethical hacking techniques.
Participants must solve each stage by uncovering hidden clues, decrypting encrypted messages, and navigating through various network challenges.
The final goal is to retrieve the secret flag and complete the mission.
## Technologies and Tools Used
The project incorporates a wide range of cybersecurity tools and concepts:
- **Wireshark** – Network packet analysis and traffic sniffing
- **Nmap** – Port scanning and service discovery
- **Gobuster** – Directory brute-forcing to uncover hidden paths
- **Socket Programming** – Creating client-server communication in Python
- **TLS/SSL Decryption** – Analyzing secure connections
- **XOR Cryptography** – Decrypting encrypted messages using symmetric encryption
## Challenge Stages
### **Stage 1: SMTP and Wireshark**
- **Objective**: Analyze a provided packet capture (PCAP) file using **Wireshark**.
- **Task**: Extract hidden information from SMTP and HTTP packets. Use the captured data to find an encrypted message and a shared secret key.
- **Hint**: Look for a `GET` request and SMTP data in the packet capture file.
### **Stage 2: Cryptography**
- **Objective**: Decrypt an XOR-encrypted message using the shared secret found in Stage 1.
- **Task**: Implement a Python script to decrypt the message. The decrypted output will reveal a link to a file hosted on a local server.
### **Stage 3: HTTP and Socket Programming**
- **Objective**: Interact with a local HTTP server using a custom client.
- **Task**: Use **Nmap** to find the server's open port. Develop a client that sends an HTTP `GET` request to the server and handles redirects to obtain the next clue.
### **Stage 4: Directory Brute-Forcing with Gobuster**
- **Objective**: Discover hidden paths on a web server.
- **Task**: Use **Gobuster** to brute-force directories and files on the server. One of the discovered pages will contain a `Client Random` value needed for the next step.
- **GitHub Link of the website**: https://github.com/eliel-monfort/CTF-Website.git
### **Stage 5: TLS Decryption**
- **Objective**: Decrypt a TLS-encrypted session using the captured data and the provided key.
- **Task**: Use **Wireshark** to analyze the decrypted session. Apply filters to locate the username and password hidden in the encrypted data.
## Completion
After completing all five stages, you'll obtain the final flag and successfully complete the mission.
## Learning Objectives
By completing this challenge, participants will enhance their understanding of:
- **Network protocols** (SMTP, HTTP, TLS)
- **Cryptography techniques**
- **Ethical hacking practices**
- **Packet analysis using Wireshark**
- **Python socket programming**
## Tips for Participants
- **Be methodical:** Each stage builds upon the previous one. Don't skip steps!
- **Use tools efficiently:** Wireshark, Nmap, and Gobuster will help uncover clues.
- **Pay attention to details:** Clues are hidden in packet captures, encrypted messages, and server responses.
## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or new challenges.
