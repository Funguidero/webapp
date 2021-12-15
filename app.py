import flask
from flask import Flask
from werkzeug.wrappers import Request, Response
app = Flask(__name__)

@app.route("/")


def home():
    app_main = """
    <h1>HOLA</h1>
    """
    return app_main


if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)

holi
