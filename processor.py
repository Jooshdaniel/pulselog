import redis
import json
import statistics
from time import sleep
from datetime import datetime

r = redis.Redis(host="redis", port=6379, decode_responses=True)

WINDOW_SIZE = 20
error_window = []

def detect_anomaly(current):
    if len(error_window) < WINDOW_SIZE:
        error_window.append(current)
        return False

    mean = statistics.mean(error_window)
    std = statistics.stdev(error_window)
    error_window.pop(0)
    error_window.append(current)

    return std > 0 and current > mean + 3 * std

while True:
    item = r.brpop("log_queue", timeout=5)
    if not item:
        sleep(0.2)
        continue

    log = json.loads(item[1])
    r.lpush("stored_logs", json.dumps(log))

    if log["level"] == "ERROR":
        current_errors = r.incr("error_count")
    else:
        current_errors = int(r.get("error_count") or 0)

    if detect_anomaly(current_errors):
        anomaly = {
            "service": log["service"],
            "error_count": current_errors,
            "timestamp": datetime.utcnow().isoformat(),
            "message": "Error spike detected"
        }
        r.lpush("anomalies", json.dumps(anomaly))
