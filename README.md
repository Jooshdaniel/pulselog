# PulseLog

PulseLog is a distributed log ingestion and monitoring backend built in Python.
It accepts logs from multiple services, processes them asynchronously, and detects abnormal error-rate spikes.

This project demonstrates backend system design, asynchronous processing, and observability concepts.

---

## Features

- Log ingestion via REST API
- Asynchronous log processing
- Error rate tracking
- Anomaly detection for traffic and error spikes
- API endpoints for querying logs and anomalies

---

## Tech Stack

- Language: Python
- Framework: FastAPI
- Asynchronous Processing
- Containerization: Docker and Docker Compose

---

## Project Structure

pulselog/
├── app/
│   ├── main.py
│   ├── ingestion/
│   ├── processing/
│   └── detection/
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## Running Locally

PulseLog is designed to run using Docker.

### Start the system

docker-compose up --build

Once running, the API will be available at:

http://localhost:8000

---

## API Documentation

Interactive API documentation is available at:

http://localhost:8000/docs
