# Pi Waker

A simple Flask web application to send Wake-on-LAN (WOL) packets to wake up computers on your local network.

## Features

- Enter a target MAC address via a web form
- Send a Wake-on-LAN packet to wake up the specified device
- Lightweight and easy to deploy on Raspberry Pi or any Linux machine

## Requirements

- Python 3
- Flask (`pip install flask`)
- `wakeonlan` utility (`sudo apt install wakeonlan` on Debian-based systems)

## Usage

download the file.

Install dependencies:

   ```bash
   pip install flask
   sudo apt install wakeonlan
   ```

Run the Flask app

   ```bash
   python app.py
   ```
Open your browser and go to
   ```bash
   http://<your-pi-ip>:5000
   ```
   
