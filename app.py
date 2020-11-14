from flask import Flask, render_template


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
        name = "Kyle"
        letters = list(name)
        return render_template("base.html", name=name, letters=letters)

    @app.route("/info")
    def info():
        return "<h1>Puppies are CUTE</h1>"

    @app.route("/puppy/<name>")
    def puppy(name):
        return f"100th letter: {name}"

    return app


if __name__ == "__main__":
    create_app()