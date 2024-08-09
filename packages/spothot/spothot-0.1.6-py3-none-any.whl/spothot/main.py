import os
import subprocess
import argparse
import platform
from spothot.app import run_flask

LOG_DIR = "/home/pi/"
LOG_FILE = os.path.join(LOG_DIR, "configure_hotspot.log")

def ensure_directory(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def ensure_log_directory():
    ensure_directory(LOG_FILE)

def log_message(message):
    ensure_log_directory()
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")
    print(message)

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        log_message(f"Command '{command}' failed with error: {e}")

def restart_services():
    log_message("Restarting services...")
    run_command('sudo systemctl restart dhcpcd')
    run_command('sudo systemctl restart dnsmasq')
    run_command('sudo systemctl restart hostapd')

def start_flask_app():
    log_message("Starting Flask app on port 80...")

    # Check if port 80 is available
    try:
        run_command("sudo lsof -i :80")
        log_message("Port 80 is in use. Please free up port 80 and try again.")
        exit(1)
    except subprocess.CalledProcessError:
        log_message("Port 80 is available. Starting Flask app...")
    
    run_flask(port=80)

def main():
    parser = argparse.ArgumentParser(description="Setup Raspberry Pi as a Wi-Fi hotspot")
    parser.add_argument('--ssid', required=True, help='SSID for the Wi-Fi hotspot')
    parser.add_argument('--password', required=True, help='Password for the Wi-Fi hotspot')
    args = parser.parse_args()

    if os.geteuid() != 0:
        log_message("Please run the script with sudo.")
        exit(1)

    log_message("Starting hotspot configuration...")

    restart_services()
    start_flask_app()

    log_message("Hotspot configuration completed.")

if __name__ == "__main__":
    main()
