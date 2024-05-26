import pytest
import logging
import sys
import os

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

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

logging.info(app.instance_path)

def titlu_film(client):
    response = client.get("/godzilla")
    return response.data




        
