import requests
import random
import time

URL = "http://localhost:8000/logs"

while True:
    level = "ERROR" if random.random() < 0.2 else "INFO"

    requests.post(URL, json={
        "service": "auth-service",
        "level": level,
        "message": "Test log"
    })

    time.sleep(0.5)
