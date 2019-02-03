# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

from flask import Flask


def create_app() -> Flask:

    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def hello():
        return "Hello World!"
    
    return app