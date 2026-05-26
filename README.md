# Multi-Threaded Python Port Scanner

A lightweight, efficient, and multi-threaded TCP port scanner written in Python. This tool allows users to scan a specific target IP address across a user-defined range of ports to identify open services quickly.

## Features

* **Multi-Threaded Execution:** Utilizes Python's `threading` module to scan up to 400 ports concurrently, significantly reducing scan times.
* **Input Validation:** Features robust validation for both IPv4 addresses (via Regular Expressions) and port ranges to ensure stable execution.
* **Thread Safety:** Implements a thread lock (`threading.Lock`) to safely append open ports to a shared list without data corruption.
* **Low Overhead:** Uses standard TCP sockets with a optimized `0.5` second timeout per port to prevent hanging on closed or filtered ports.

---

## How It Works

1. **IP Validation:** The script prompts for a target IP address and validates it against a strict IPv4 regex pattern.
2. **Port Range Validation:** The user provides a range (e.g., `20-80`). The script ensures the range is formatted correctly, falls within valid port boundaries (`0-65535`), and that the minimum port is less than or equal to the maximum port.
3. **Threading Pool:** The script spawns threads to check individual ports using `socket.connect_ex()`. It manages these in batches defined by `NUM_THREADS` (default: 400).
4. **Reporting:** Once the scan is complete, it outputs a list of all detected open ports.

---

## Usage

1. Clone or download the script to your local machine.
2. Open your terminal or command prompt and run:

```bash
python port_scanner.py
