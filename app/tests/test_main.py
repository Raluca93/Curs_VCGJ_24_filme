import pytest
import logging
import sys
import os

from main import app
from lib import biblioteca_filme as biblioteca

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

@pytest.fixture
def client():
    # Creere de client pentru aplicatia Flask pentru testare
    with app.test_client() as client:
        app.config.update({
        "TESTING": True,
    })
        yield client
        
logger = logging.getLogger(__name__)

def test_title(client):
    
    logger.info("Trimitere cerere GET către /godzilla")
    # Send a GET request to the specified static file
    # Check that the status code is 200
    ans_data = biblioteca.titlu_film(client)
    # Check that the response contains some expected content from the CSS file
    expected_content = b"<h1>Godzilla</h1>"
    if (expected_content in ans_data):
        logger.info("Pagine WEB conține titlul așteptat")
        assert True
    else:
        logger.error(f"Pagina WEB nu raspunde cu titlul așteptat, ci cu {ans_data}")
        assert False