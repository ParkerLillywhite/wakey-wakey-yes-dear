import requests
import time

# Your website URL
URL = "https://yourwebsite.com"

def ping_website():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("Yes dear...")
        else:
            print(f"Sooo sleepy... Dreams: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Soooo sleepy... Dreams: {e}")

# Run indefinitely, pinging every 5 minutes (300 seconds)
while True:
    ping_website()
    time.sleep(900)
