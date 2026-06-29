from flask import Flask
import logging
import threading
import time

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    logging.info("HTTP request received")
    return "Hello from Kubernetes!"

def heartbeat():
    while True:
        logging.info("Application heartbeat")
        time.sleep(10)

threading.Thread(target=heartbeat, daemon=True).start()

app.run(host="0.0.0.0", port=5000)
