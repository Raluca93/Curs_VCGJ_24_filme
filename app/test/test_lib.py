import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("/home/ion/proiect/Curs_VCGJ_24_filme/app")
from lib import lib_filme as filme



def test_descriere_film():
    descriere = filme.descriere_film()

    if "icon of popular culture" in descriere:
        logger.info(f"Functia descriere_film functioneaza corect: {descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_film NU functioneaza corect: {descriere}")
        assert False

def test_quotes():
    quotes = filme.quotes()

    if "scientifically known as Euterpe oleracea" in descriere:
        logger.info(f"Functia descriere_acai functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_acai NU functioneaza corect:\n{descriere}")
        assert False 
