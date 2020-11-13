from flask import Flask


def create_app():
    """
    Create a Flask app using the app factory pattern

    Return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    @app.route("/")
    def index():
        """
        Render a Hello World response

        Return: Flask response
        """
        return "<h1>Hello Puppy!</h1>"

    @app.route("/info")
    def info():
        return "<h1>Puppies are CUTE</h1>"

    return app


if __name__ == "__main__":
    create_app()