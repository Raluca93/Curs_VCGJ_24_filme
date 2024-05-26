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
logging.info(app.instance_path)
def test_incarcare_trailer(client):
    response = client.get("/mazerunner/trailer")
    logger.info("TEST TRAILER -> Trimitere cerere GET către /mazerunner/trailer")
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

def test_style_css(client):
    # Set up the test client
    logger.info("TEST STYLE -> Trimitere cerere GET către /static/css/style.css")
        
    # Send a GET request to the specified static file
    response = client.get('/static/style.css')
        
    # Check that the status code is 200
    if(response.status_code == 200):
        logger.info("Codul de stare HTTP este 200 pentru style.css")
        assert True
    else:
        logger.error(f"Status code nu este 200 OK, Received STATUS = {response.status_code}")
        assert False
    
    # Check that the response contains some expected content from the CSS file
    expected_content = b"background-image: url('../static/images/maze-background.jpg');"
    if (expected_content in response.data):
        logger.info("Fisierul CSS conține textul asteptat")
        assert True
    else:
        logger.error("Continutul CSS asteptat nu se afla in raspuns")
        assert False


    

    