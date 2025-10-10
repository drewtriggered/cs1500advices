import requests
import datetime
import time

LOG_FILE = "Drew.Trigg.advices"

while True:
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        data = response.json()
        advice = data["slip"]["advice"]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {advice}\n")

        print(f"Advice logged at {timestamp}: {advice}")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(3600)  # 1 hour

