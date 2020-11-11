from flask import Flask


def create_app():
    """
    Create a Flask app using the app factory pattern

    Return: Flask app
    """

    app = Flask(__name__)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    @app.route("/")
    def index():
        """
        Render a Hello World response

        Return: Flask response
        """
        return "Hello World!"

    return app


if __name__ == "__main__":
    create_app()