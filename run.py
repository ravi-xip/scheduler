import logging

from flask import Flask
from flask_cors import CORS


def create_app():
    """
    Sets up the Flask app.
    :return: a handle to the Flask app.
    """
    app = Flask(__name__)
    app.config["CORS_HEADERS"] = "Content-Type"
    CORS(
        app,
        resources={
            r"/*": {"origins": ["http://localhost:3000", "https://ravi-xip.ngrok.io"]}
        },
    )
    return app


def start_flask_server():
    """
    Starts the Flask server.
    """
    app = create_app()

    # Create a route for the root of the app
    @app.route("/", methods=["GET"])
    def ping():
        return "Scheduler\n", 200

    @app.route("/add", methods=["GET"])
    def add():
        return "Scheduling Add\n", 200

    # Start the server
    app.run(host="0.0.0.0", port=8080, debug=False)


if __name__ == "__main__":
    logging.info(f"Starting the flask server")
    start_flask_server()
