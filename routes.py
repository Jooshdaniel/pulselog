from fastapi import APIRouter
import redis
import json
from datetime import datetime

router = APIRouter()
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@router.post("/logs")
def ingest_log(log: dict):
    log["timestamp"] = log.get("timestamp") or datetime.utcnow().isoformat()
    r.lpush("log_queue", json.dumps(log))
    return {"status": "accepted"}

@router.get("/logs")
def get_logs():
    logs = r.lrange("stored_logs", 0, 100)
    return [json.loads(l) for l in logs]

@router.get("/anomalies")
def get_anomalies():
    anomalies = r.lrange("anomalies", 0, 50)
    return [json.loads(a) for a in anomalies]
