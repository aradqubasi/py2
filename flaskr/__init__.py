import os

from flask import Flask

def create_app(test_config=None)->Flask:
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRECT_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqllite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, Azure Webapp'

    return app