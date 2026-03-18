import os

from flask import Flask

import psycopg2
import socket
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "flask_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "flask_request_latency_seconds",
    "Request latency"
)

@app.route("/")
def hello():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()

    with REQUEST_LATENCY.time():
        db_status = check_db_connection()
        hostname = socket.gethostname()
        return f"{db_status} from {hostname}"
     
def check_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DATABASE_HOST"),
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            port=os.getenv("DATABASE_PORT")
        )
        conn.close()
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"

# def hello_world():
#      REQUEST_COUNT.labels(method="GET", endpoint="/").inc()

#      with REQUEST_LATENCY.time():
#          hostname = socket.gethostname()
#          return f"{check_db_connection()} from {hostname}"
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
