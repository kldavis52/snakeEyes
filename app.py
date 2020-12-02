from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


def create_app():
    """
    Create a Flask app using the app factory pattern

    Return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config["SECRET_KEY"] = "mysecretkey"
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    class InfoForm(FlaskForm):
        breed = StringField(label="What Breed are you?")
        submit = SubmitField(label="Submit")

    @app.route("/", methods=["Get", "POST"])
    def home():
        """
        Render a Hello World response

        Return: Flask response
        """
        breed = False

        form = InfoForm()
        if form.validate_on_submit():
            breed = form.breed.data
            form.breed.data = ""

        return render_template("snakeeyes/home.html")

    @app.route("/signup_form")
    def signup_form():
        return render_template("snakeeyes/signup.html")

    @app.route("/thankyou")
    def thankyou():
        first = request.args.get("first")
        last = request.args.get("last")
        return render_template("snakeeyes/thankyou.html", first=first, last=last)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("snakeeyes/404.html"), 404

    return app


if __name__ == "__main__":
    create_app()