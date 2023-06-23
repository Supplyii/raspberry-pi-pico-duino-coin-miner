import requests
import time

# DuinoCoin API endpoint
API_URL = "https://server.duinocoin.com"

# Mining parameters
HASHRATE_MULTIPLIER = 1000  # Increase this if the mining process is too slow
TARGET_DIFFICULTY = 250  # Adjust this according to your mining performance

# DuinoCoin account credentials
username = input("Enter your DuinoCoin username: ")
password = input("Enter your DuinoCoin password: ")

# Function to mine DuinoCoin
def mine_duinocoin():
    global username, password
    try:
        result = {}  # Initialize result with an empty dictionary
        while True:
            response = requests.get(f"{API_URL}/mine.php", params={
                "username": username,
                "password": password,
                "difficulty": TARGET_DIFFICULTY
            })
            if response.status_code == 200:
                try:
                    result = response.json()
                    if result.get("success"):
                        print("Hashrate:", result["hashrate"], "H/s")
                        print("Accepted shares:", result["accepted"])
                        print("Rejected shares:", result["rejected"])
                    else:
                        print("Mining error:", result["message"])
                except ValueError:
                    print("Invalid JSON response:", response.content)
            else:
                print("API request error:", response.status_code)
            time.sleep(1 / (result.get("hashrate", 1) * HASHRATE_MULTIPLIER))
    except Exception as e:
        print("An error occurred:", e)

# Start mining
mine_duinocoin()
