import pytest
import sys

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
    response = client.get("/mazerunner/trailer")
    # Verificare cod de stare
    assert response.status_code == 200
    # Verificare link clip video 
    assert b'src="https://www.youtube.com/embed/64-iSYVmMVY?si=Fe-B7y-cTZPSqbTx"' in response.data, f"Videoclipul nu a fost incarcat corect"