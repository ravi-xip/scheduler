import logging

from flask import Flask
from flask_cors import CORS
from tasks import add_t


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

    @app.route("/add/<num_1>/<num_2>", methods=["GET"])
    def add(num_1, num_2):
        # Schedule an add task

        # Wait for the task to complete and return the result
        # Convert the input to integers
        num_1 = int(num_1)
        num_2 = int(num_2)

        add_result = add_t.delay(num_1, num_2)
        add_result.wait()
        return f"Result: {add_result.get()}\n", 200

    # Start the server
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    logging.info(f"Starting the flask server")
    start_flask_server()
