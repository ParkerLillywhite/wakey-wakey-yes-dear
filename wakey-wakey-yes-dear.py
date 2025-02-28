import requests
import time

URL = "https://fell-beast-apothecary.onrender.com"

def ping_website():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("Yes dear...")
        else:
            print(f"Sooo sleepy... Dreams: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Soooo sleepy... Dreams: {e}")

ping_website()
