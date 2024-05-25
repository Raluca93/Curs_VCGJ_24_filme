import pytest
import logging
import sys
logger = logging.getLogger(__name__)
sys.path.insert(0, '../')

from filme import app

@pytest.fixture
def client():
    # Creere de client pentru aplicatia Flask pentru testare
    with app.test_client() as client:
        app.config.update({
        "TESTING": True,
    })
        yield client

def test_incarcare_trailer(client):
    response = client.get("/mazerunner/trailer/ERROR")
    # Verificare cod de stare
    if (response.status_code == 200):
        logging.info(f"Status 200 OK, conform asteptarilor.")
        assert True
    else:
        logging.error(f"Status code nu este 200 OK, Received STATUS = {response.status_code}")
        assert False
    # Verificare link clip video 
    
    if (b'src="https://www.youtube.com/embed/64-iSYVmMVY?si=Fe-B7y-cTZPSqbTx"' in response.data):
        logging.info("Link-ul video este corect si incarcat cu succes.")
        assert True
    else:
        logging.error(f"Videoclipul nu a fost incarcat corect")
        assert False

    