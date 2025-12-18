# PulseLog

PulseLog is a distributed log ingestion and anomaly detection system built in Python.

## What It Does
- Accepts logs via a REST API
- Processes logs asynchronously
- Tracks error rates
- Detects abnormal spikes
- Exposes logs and anomalies via API

## Running PulseLog
```bash
docker-compose up --build
