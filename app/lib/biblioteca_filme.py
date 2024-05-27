import pytest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from filme import app

@pytest.fixture
def client():
    # Creere de client pentru aplicatia Flask pentru testare
    with app.test_client() as client:
        app.config.update({
        "TESTING": True,
    })
        yield client

logger = logging.getLogger(__name__)
logging.info(app.instance_path)



logging.info(app.instance_path)

def trailer_status(client):
    response = client.get("/mazerunner/trailer")
    return response.status_code

def trailer_data(client):
    response = client.get("/mazerunner/trailer")
    return response.data

def css_status(client):
    response = client.get("/static/style.css")
    return response.status_code

def css_data(client):
    response = client.get("/static/style.css")
    return response.data

def titlu_film(client):
    response = client.get("/mazerunner")
    return response.data