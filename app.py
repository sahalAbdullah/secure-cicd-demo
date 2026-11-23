import os
import socket
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template

app = Flask(__name__)
STARTED = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


@app.get("/")
def index():
    photo = os.path.exists(os.path.join(app.static_folder, "profile.png"))
    return render_template(
        "index.html",
        commit=os.environ.get("GIT_SHA", "local")[:7],
        host=socket.gethostname(),
        started=STARTED,
        photo=photo,
    )


@app.get("/health")
def health():
    return jsonify(status="ok")
