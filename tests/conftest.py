import pytest
import os

from flask import Flask

from flaskr import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTTING': True
    })
    yield app

@pytest.fixture
def client(app: Flask):
    return app.test_client()