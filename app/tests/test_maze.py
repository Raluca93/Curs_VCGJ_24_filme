import logging
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from filme import app
from app.lib import biblioteca_filme_maze as biblioteca

@pytest.fixture
def client():
    # Creere de client pentru aplicatia Flask pentru testare
    with app.test_client() as client:
        app.config.update({
        "TESTING": True,
    })
        yield client
logger = logging.getLogger(__name__)

def test_incarcare_trailer(client):
    rsp = biblioteca.trailer_status(client)
    if rsp == 200:
        logging.info("Status 200 OK, conform asteptarilor.")
        assert True
    else:
        logging.error("Status code nu este 200 OK, Received STATUS = {1}".format(rsp))
        assert False
    rsp_data = biblioteca.trailer_data(client)

    if b'src="https://www.youtube.com/embed/64-iSYVmMVY?si=Fe-B7y-cTZPSqbTx"' in rsp_data:
        logging.info("Link-ul video este corect si incarcat cu succes.")
        assert True
    else:
        logging.error("Videoclipul nu a fost incarcat corect")
        assert False

def test_style_css(client):    
    logger.info("Trimitere cerere GET către /static/css/style.css")
    rsp = biblioteca.css_status(client)
    # Check that the status code is 200
    if rsp == 200:
        logger.info("Codul de stare HTTP este 200 pentru style.css")
        assert True
    else:
        logger.error(f"Expected status code 200, but got {rsp}")
        assert False
    rsp_data = biblioteca.css_data(client)
    # Check that the response contains some expected content from the CSS file
    expected_content = b"background-image: url('../static/images/maze-background.jpg');"
    if expected_content in rsp_data:
        logger.info("Fișierul CSS conține textul așteptat")
        assert True
    else:
        logger.error("Expected CSS content not found in response")
        assert False

def titlu_film(client):
    logger.info("Trimitere cerere GET către /mazerunner")
    rsp_data = biblioteca.titlu_film(client)
    expected_content = b"<h1>Maze Runner</h1>"
    if expected_content in rsp_data:
        logger.info("Pagine WEB conține titlul așteptat")
        assert True
    else:
        logger.error("Pagina WEB nu raspunde cu titlul așteptat")
        assert False