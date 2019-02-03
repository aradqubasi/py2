from flaskr import create_app
from flask.testing import FlaskClient

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_client(client: FlaskClient):
    assert b'Hello, Azure Webapp' in client.get('/hello').data