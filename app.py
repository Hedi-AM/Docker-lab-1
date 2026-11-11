import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    message = os.environ.get("WELCOME_MESSAGE", "Bonjour depuis la version 1.0.1 !")
    return f"<h1>{message}</h1>"


if __name__ == "__main__":
    # host="0.0.0.0" is REQUIRED inside a container.
    # If you use "127.0.0.1", the app is only reachable *inside* the container
    # and curl from your computer will never get a response.
    app.run(host="0.0.0.0", port=5000)
